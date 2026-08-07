# Development state - August 7 2026

## Current Development

Version: 0.10.4

Focus:
Customization improvements.

Planned improvements:

* Particle system customization:
  * Adjustable particle count.
  * Selectable particle styles (circle, square, star).
  * Selectable particle movement patterns.

* Icon customization:
  * Adjustable icon density.
  * Adjustable icon size while preserving depth-based scaling.

* Animation customization:
  * Adjustable animation intensity.
  * Preserve existing organic movement behaviour.

## Completed

### Version 0.10.3

* Added individual icon breathing variation.
* Refined screensaver animation behaviour.
* Added demonstration video documentation.
* Improved README and development documentation.
* Corrected Debian package installation instructions.

Completed releases:

- v0.10.3 Animation and documentation polish release completed.
- v0.10.2 Visual Polish Release completed.
- Release restored depth-based icon scaling and opacity variation.
- Screenshots updated to reflect current rendering behaviour.
- Debian package and documentation updated.

Latest important commits:

- v0.10.3 release commits:
  - Add individual icon breathing variation.
  - Refine screensaver animation behaviour.
  - Add screensaver demo video documentation.
  - Update README and development documentation.
  - Correct Debian package installation instructions.

- v0.10.2 release commits:
  - Restore icon depth and fade animation behaviour.
  - Update screenshots for restored icon animations.
  - Update changelog and Debian packaging metadata.
  - Bump version to 0.10.2.
  - Update development state for release.

Completed features:

- Standalone visual screensaver application.
- Cinnamon integration without replacing lock handling.
- Debian package build and installation workflow.
- Standalone installer workflow.
- GPLv3 licensing documentation.
- User configuration support.
- GTK settings application.
- Settings application launcher and desktop menu entry.
- Configurable animation speed.
- Configurable mouse exit behaviour.
- Configurable background colour.
- Animated background colour transition.
- Floating SVG device icons.
- Particle background effects.
- Icon fade-in animation.
- Icon depth variation.
- Device-specific icon behaviours.

Current v0.10.4 goals:

- Add particle system customization.
- Add icon density controls.
- Add animation intensity controls.
- Preserve existing depth-based icon scaling behaviour.
- Improve user control without reducing organic animation quality.

Planned customization improvements:

- Add particle count controls.
- Add particle style selection.
- Add particle movement pattern selection.
- Add icon density controls.
- Add icon size customization while preserving depth simulation.
- Add animation intensity adjustment.

Testing completed:

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

- Latest release:

  mint-device-screensaver_0.10.3_all.deb

- Build command:

  debian/build-deb.sh

Next tasks:

1. Implement particle customization settings.
2. Add icon density controls.
3. Add animation intensity controls.
4. Review icon size customization while preserving depth scaling.
5. Update screenshots and documentation after feature completion.
6. Prepare v0.10.4 release.

Development notes:

- Do not replace Cinnamon's lock/login handling.
- The application should remain a standalone visual screensaver.
- Cinnamon integration should launch the animation only and allow Cinnamon to manage security features.
- Preserve the existing GTK settings architecture.
- Avoid major rendering changes unless they provide a clear visual improvement.
- Preserve the organic movement and depth perception introduced in previous releases.
