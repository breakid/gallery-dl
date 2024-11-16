# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import datetime

from gallery_dl.extractor import pillowfort

__tests__ = (
    {
        "#url": "https://www.pillowfort.social/posts/27510",
        "#category": ("", "pillowfort", "post"),
        "#class": pillowfort.PillowfortPostExtractor,
        "#pattern": r"https://img\d+\.pillowfort\.social/posts/\w+_out\d+\.png",
        "#count": 4,
        "avatar_url": str,
        "col": 0,
        "commentable": True,
        "comments_count": int,
        "community_id": None,
        "content": str,
        "count": 4,
        "created_at": str,
        "date": datetime.datetime,
        "deleted": None,
        "deleted_at": None,
        "deleted_by_mod": None,
        "deleted_for_flag_id": None,
        "embed_code": None,
        "id": int,
        "last_activity": str,
        "last_activity_elapsed": str,
        "last_edited_at": str,
        "likes_count": int,
        "media_type": "picture",
        "nsfw": False,
        "num": range(1, 4),
        "original_post_id": None,
        "original_post_user_id": None,
        "picture_content_type": None,
        "picture_file_name": None,
        "picture_file_size": None,
        "picture_updated_at": None,
        "post_id": 27510,
        "post_type": "picture",
        "privacy": "public",
        "reblog_copy_info": list,
        "rebloggable": True,
        "reblogged_from_post_id": None,
        "reblogged_from_user_id": None,
        "reblogs_count": int,
        "row": int,
        "small_image_url": None,
        "tags": list,
        "time_elapsed": str,
        "timestamp": str,
        "title": "What is Pillowfort.social?",
        "updated_at": str,
        "url": r"re:https://img3.pillowfort.social/posts/.*\.png",
        "user_id": 5,
        "username": "Staff",
    },
    {
        "#url": "https://www.pillowfort.social/posts/1124584",
        "#comment": "'b2_lg_url' media URL (#4570)",
        "#category": ("", "pillowfort", "post"),
        "#class": pillowfort.PillowfortPostExtractor,
        "#pattern": r"https://img2\.pillowfort\.social/posts/c8e834bc09e6_Brandee\.png",
        "#count": 1,
        "avatar_frame": None,
        "avatar_id": None,
        "avatar_url": "https://img3.pillowfort.social/avatars/000/037/139/original/437.jpg?1545015697",
        "b2_lg_url": "https://img2.pillowfort.social/posts/c8e834bc09e6_Brandee.png",
        "b2_sm_url": "https://img2.pillowfort.social/posts/c8e834bc09e6_Brandee_small.png",
        "cached_tag_list": "art, digital art, mermaid, mermaids, underwater, seaweed, illustration, speed paint",
        "col": 0,
        "comm_screening_status": "not_applicable",
        "commentable": True,
        "comments_count": 0,
        "community_id": None,
        "concealed_comment_warning": None,
        "content": "<p>Sea Bed</p>",
        "count": 1,
        "created_at": r"re:2020-02-.+",
        "currentuser_default_avatar_url": None,
        "currentuser_multi_avi": None,
        "date": "dt:2020-02-29 17:09:03",
        "deleted": None,
        "deleted_at": None,
        "deleted_by_mod": None,
        "deleted_for_flag_id": None,
        "embed_code": None,
        "extension": "png",
        "filename": "Brandee",
        "hash": "c8e834bc09e6",
        "id": 720167,
        "last_activity": r"re:2020-02-.+",
        "last_activity_elapsed": r"re:\d+ months",
        "last_edited_at": None,
        "likes_count": 8,
        "media_type": "picture",
        "nsfw": False,
        "num": 1,
        "original_post_id": None,
        "original_post_user_id": None,
        "pic_row_last": 1,
        "picture_content_type": None,
        "picture_file_name": None,
        "picture_file_size": None,
        "picture_updated_at": None,
        "post_id": 1124584,
        "post_type": "picture",
        "privacy": "public",
        "reblog_copy_info": [],
        "rebloggable": True,
        "reblogged_from_post_id": None,
        "reblogged_from_user_id": None,
        "reblogs_count": int,
        "row": 1,
        "small_image_url": None,
        "tag_list": None,
        "tags": [
            "art",
            "digital art",
            "mermaid",
            "mermaids",
            "underwater",
            "seaweed",
            "illustration",
            "speed paint",
        ],
        "time_elapsed": r"re:\d+ months",
        "timestamp": str,
        "title": "",
        "updated_at": r"re:2020-02-.+",
        "url": "",
        "user_concealed": None,
        "user_id": 37201,
        "username": "Maclanahan",
    },
    {
        "#url": "https://www.pillowfort.social/posts/1557500",
        "#comment": "'external' option",
        "#category": ("", "pillowfort", "post"),
        "#class": pillowfort.PillowfortPostExtractor,
        "#options": {
            "external": True,
            "inline": False,
        },
        "#pattern": r"https://twitter\.com/Aliciawitdaart/status/1282862493841457152",
    },
    {
        "#url": "https://www.pillowfort.social/posts/1672518",
        "#comment": "'inline' option",
        "#category": ("", "pillowfort", "post"),
        "#class": pillowfort.PillowfortPostExtractor,
        "#options": {"inline": True},
        "#count": 3,
    },
    {
        "#url": "https://www.pillowfort.social/Pome",
        "#category": ("", "pillowfort", "user"),
        "#class": pillowfort.PillowfortUserExtractor,
        "#pattern": r"https://img\d+\.pillowfort\.social/posts/",
        "#range": "1-15",
        "#count": 15,
    },
    {
        "#url": "https://www.pillowfort.social/Staff/tagged/funding",
        "#category": ("", "pillowfort", "user"),
        "#class": pillowfort.PillowfortUserExtractor,
        "#pattern": r"https://img\d+\.pillowfort\.social/posts/",
        "#count": range(30, 50),
    },
)
