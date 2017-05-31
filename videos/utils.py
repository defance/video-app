from __future__ import unicode_literals

from collections import defaultdict
from django.core.files.storage import DefaultStorage
from django.utils.translation import pgettext_lazy as _p, ugettext_lazy as _u
from re import search as re_search
from subprocess import check_output

from .models import Video

TIME_DICT = {
    'h': _p('duration', 'hrs'),
    'm': _p('duration', 'min'),
    's': _p('duration', 'sec')
}


def get_video_info(video):
    """
    Execute ffprobe and extract file info in following format:

    >> duration=XX:XX:XX.XXXXXXX
    >> height=XXX
    >> width=XXX

    Return output as string.

    :param video: (Video) Video to extract info about
    :return: (str) Extracted info of duration, height and width
    """
    return check_output([
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration', '-sexagesimal',
        '-show_entries', 'stream=height,width',
        '-of', 'default=noprint_wrappers=1', video.video.path
    ])


def extract_raw_duration_info(output):
    """
    Extract rew duration info from ffprobe output. Returns str containing video
    duration in format:

    >> hours:minutes:seconds.micros

    :param output: (str) Previous output of ffprobe
    :return: (str) Str with durations
    """
    re_exp = 'duration=(\d*:\d*:\d*\.\d)'
    return re_search(re_exp, output).groups()[0]


def extract_duration_info(output):
    """
    Extract duration info from ffprobe output. Returns dict containing video
    duration in hours (h), minutes (m) and seconds (s).

    :param output: (str) Previous output of ffprobe
    :return: (dict: str => float) Dict with durations
    """
    re_exp = '(?P<h>\d*):(?P<m>\d*):(?P<s>\d*.\d*)'
    re_res = re_search(re_exp, output)
    return dict(map(
        lambda (key, val): (key, float(val)),
        re_res.groupdict().items()
    )) if re_res else {}


def get_duration_str(info):
    """
    Builds duration string with duration info.

    Note: it is language-dependant.

    :param info: (dict: str -> float)
    :return: (str)
    """
    def get_desc(key):
        return "%(dur).2f %(desc)s" % {
            'dur': info[key],
            'desc': TIME_DICT[key]
        } if info[key] > 0 else ''
    return ' '.join(map(get_desc, ['h', 'm', 's'])) if info else _u('Unknown')


def generate_video_thumbnail(video, size=150):
    """
    Executes ffmpeg to create thumbnail and saves it to static with a name of:

    >> media_dir/preview/video_id.png

    :param video: (Video) Video to create preview of
    :param size: (int) Dimensional size (in px) of thumbnail, greater than 0,
                       default 150
    :return: Nothing
    """
    storage = DefaultStorage()
    short_name = storage.get_available_name('preview/%s.png' % video.id)
    filename = storage.path(short_name)
    check_output([
        'convert',  video.video.path+'[1]',
        '-resize', '{size}x{size}^'.format(size=size),
        '-gravity', 'center',
        '-extent', '{size}x{size}'.format(size=size),
        filename
    ])
    video.preview = short_name


def process_video(video):
    try:
        video.status = 'processing'
        video.save()
        output = get_video_info(video)
        video.duration = extract_raw_duration_info(output)
        generate_video_thumbnail(video)
        video.status = 'ready'
        video.save()
    except Exception:
        video.status = 'error'
        video.save()
        return False
    return True


def process_videos(process=False):
    """
    Process videos. Update its duration and create thumbnail.

    :param process: (bool) Whether do the actual processing
    :return: (int) Number of videos processed
    """

    videos = Video.objects.filter(status__in=['loaded', 'queued'])
    report = defaultdict(int)

    for video in videos:
        if video.status != 'queued':
            video.status = 'queued'
            video.save()

    for video in videos:
        if video.status == 'queued':
            report[process_video(video) if process else True] += 1

    return report
