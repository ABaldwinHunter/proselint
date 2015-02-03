"""WGD100: Weasel words.

---
layout:     post
error_code: WGD200
source:     write-good
source_url: https://github.com/btford/write-good
title:      Weasel words.
date:       2014-06-10 12:31:19
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""


def check(text):

    error_code = "WGD200"
    msg = "Weasel words present."

    return [(1, 1, error_code, msg)]