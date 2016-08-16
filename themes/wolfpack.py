class WolfpackColor:
    """
    This theme is inspired by https://github.com/carlson-erik/wolfpack
    """
    USERNAME_FG = 250  # very light grey
    USERNAME_BG = 240  # grey
    USERNAME_ROOT_BG = 167 # pink/red

    HOSTNAME_FG = 250  # very light grey
    HOSTNAME_BG = 238  # darker grey

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 116  # very light blue
    HOME_FG = 0  # black
    PATH_BG = 237  # dark grey
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 167  # pink/red
    READONLY_FG = 254  # nearly-white grey

    SSH_BG = 24  # blue
    SSH_FG = 254  # nearly-white grey

    REPO_CLEAN_BG = 86  # light green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 74  # light blue
    REPO_DIRTY_FG = 0  # black

    JOBS_FG = 74  # light blue
    JOBS_BG = 238  # darker grey

    CMD_PASSED_BG = 236  # darker grey
    CMD_PASSED_FG = 15  # light grey
    CMD_FAILED_BG = 167  # pink/red
    CMD_FAILED_FG = 15  # light grey

    SVN_CHANGES_BG = 238  # darker grey
    SVN_CHANGES_FG = 86  # light green

    GIT_AHEAD_BG = 240  # grey
    GIT_AHEAD_FG = 250  # very light grey
    GIT_BEHIND_BG = 240
    GIT_BEHIND_FG = 250
    GIT_STAGED_BG = 86  # light green
    GIT_STAGED_FG = 0  # black
    GIT_NOTSTAGED_BG = 158  # very light green
    GIT_NOTSTAGED_FG = 0
    GIT_UNTRACKED_BG = 135  # purple
    GIT_UNTRACKED_FG = 0
    GIT_CONFLICTED_BG = 167  # pink/red
    GIT_CONFLICTED_FG = 15

    VIRTUAL_ENV_BG = 86  # light green
    VIRTUAL_ENV_FG = 0

class Color(WolfpackColor):
    """
    This subclass is required when the user chooses to use 'wolfpack' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass
