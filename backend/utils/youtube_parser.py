from youtube_transcript_api import (
    YouTubeTranscriptApi
)

def get_video_id(url):

    if "watch?v=" in url:
        return url.split("watch?v=")[1]

    return url.split("/")[-1]

def extract_youtube_text(url):

    video_id = get_video_id(url)

    transcript = (
        YouTubeTranscriptApi
        .get_transcript(video_id)
    )

    text = ""

    for item in transcript:
        text += item["text"] + " "

    return [
        {
            "source": "YouTube",
            "reference": "Transcript",
            "text": text
        }
    ]