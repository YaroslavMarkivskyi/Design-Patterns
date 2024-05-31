"""
Client code to create ui on different platform.
"""

from creational_patterns.abstract_factory.crossplatform_app\
    .factories.desktop_factories import (
        LinuxHelpWindow,
        LinuxSettingsWindow,
        LinuxMainWindow,

        WindowsMainWindow,
        WindowsHelpWindow,
        WindowsSettingsWindow,

        MacMainWindow,
        MacHelpWindow,
        MacSettingsWindow,
    )
from creational_patterns.abstract_factory.crossplatform_app\
    .factories.mobile_factories import (
        AndroidHelpWindow,
        AndroidSettingsWindow,
        AndroidMainWindow,

        IosMainWindow,
        IosHelpWindow,
        IosSettingsWindow,
    )
from creational_patterns.abstract_factory.crossplatform_app\
    .factories.web.web_factory import (
        WebHelpWindow,
        WebMainWindow,
        WebSettingsWindow
    )

from creational_patterns.abstract_factory.crossplatform_app\
    .ui.base import (
        HelpWindow,
        SettingsWindow,
        MainWindow
    )


def use_main_window(main_window: MainWindow) -> None:
    main_window.open_help()
    main_window.close_help()

    main_window.open_settings()
    main_window.close_settings()

    main_window.close_window()


def use_settings_window(settings_window: SettingsWindow) -> None:
    settings_window.open_window()
    settings_window.close_window()

    settings_window.open_help()
    settings_window.close_help()

    settings_window.close_settings()


def use_help_window(help_window: HelpWindow) -> None:
    help_window.open_window()
    help_window.close_window()

    help_window.open_settings()
    help_window.close_settings()

    help_window.close_help()


def create_platform(main_window: MainWindow,
                    settings_window: SettingsWindow,
                    help_window: HelpWindow,
                    ):
    """Method that has business logic to create linux ui."""
    print(":::::UI main window::::::::::::")
    use_main_window(main_window)
    print("::::UI settings window::::::::")
    use_settings_window(settings_window)
    print("::::UI help window:::::::::::")
    use_help_window(help_window)


if __name__ == "__main__":
    platforms = {
        "linux": (
            LinuxMainWindow(),
            LinuxSettingsWindow(),
            LinuxHelpWindow()
        ),
        "windows": (
            WindowsMainWindow(),
            WindowsSettingsWindow(),
            WindowsHelpWindow()
        ),
        "mac": (
            MacMainWindow(),
            MacSettingsWindow(),
            MacHelpWindow()
        ),
        "android": (
            AndroidMainWindow(),
            AndroidSettingsWindow(),
            AndroidHelpWindow()
        ),
        "ios": (
            IosMainWindow(),
            IosSettingsWindow(),
            IosHelpWindow()
        ),
        "web": (
            WebMainWindow(),
            WebSettingsWindow(),
            WebHelpWindow()
        ),
    }

    for key, value in platforms.items():
        print(f"Platform {key}: ")
        create_platform(*value)
        print("/////////////////\n")
