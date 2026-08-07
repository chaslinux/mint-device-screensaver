# Development state - August 7 2026

Current milestone:
- v0.10.0 user experience improvements in progress.
- Configuration backend now supports saving changes.
- Standalone GTK settings application added.
- Settings application has its own launcher and desktop menu entry.
- Debian packaging updated to include settings application.

Latest important commits:
- 39b1e50 Add configuration save support
- Add settings application skeleton

Completed features:
- Standalone visual screensaver application.
- Cinnamon integration without replacing lock handling.
- Debian package build and installation workflow.
- Standalone installer workflow.
- GPLv3 licensing documentation.
- User configuration support.
- GTK settings application foundation.

Current v0.10.0 goals:
- Add animation speed control.
- Add mouse movement behavior setting.
- Add background color selection.
- Improve first-run user experience.

Verified:
- Command line help:

  mint-device-screensaver --help

- Version reporting:

  mint-device-screensaver --version

- Desktop entry validation:

  desktop-file-validate /usr/share/applications/mint-device-screensaver.desktop

- Manual launch:

  cinnamon-screensaver-command --activate

- CTRL+ALT+L lock flow works.
- Cinnamon lock screen appears after screensaver activation.
- Unlock returns correctly to the Cinnamon session.
- Cinnamon retains responsibility for authentication.

Logs:
- ~/.local/state/mint-device-screensaver/mint-device-screensaver.log

Package:
- Debian package:

  mint-device-screensaver_0.1.0_all.deb

- Build command:

  debian/build-deb.sh

Next tasks:
1. Improve README/install instructions.
2. Add screenshots/demo media.
3. Review configuration options.
4. Prepare v0.1.2 release.
5. Continue testing on additional hardware/displays if available.

Development notes:
- Do not replace Cinnamon's lock/login handling.
- The application should remain a standalone visual screensaver.
- Cinnamon integration should launch the animation only and allow Cinnamon to manage security features.
- Do not restart rendering work unless a real rendering bug appears.

Installer:
- Added top-level install.sh convenience installer.
- Installer builds and installs the Debian package.
- Installer does not modify Cinnamon screensaver or lock settings.
- Mint Device Screensaver remains a standalone visual application.
