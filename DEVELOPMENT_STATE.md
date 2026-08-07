# Development state - August 7 2026

## Current milestone

- v0.10.1 released.
- Release workflow verified from development through Debian package installation.
- Project documentation and screenshots updated.

## Latest release

Release:

- v0.10.1

Tag:

- v0.10.1

Release highlights:

- Added user configuration support.
- Added standalone GTK settings application.
- Added settings launcher and desktop menu integration.
- Added background colour selection.
- Added animation speed control.
- Added mouse movement behaviour setting.
- Added dynamic background colour transitions.
- Improved README documentation.
- Added project screenshots.
- Added CHANGELOG.md.

## Known observations / possible regressions
Investigation result:
- Icon depth and fade behaviour changed during later rendering improvements.
- v0.7-staggered-icons contained stronger depth-based scaling and opacity variation.
- Current version retained fade logic but reduced depth visual differences.
- Restore enhanced icon depth behaviour as a future visual polish task.

## Completed features
### Application

- Standalone visual screensaver application.
- GTK and Clutter based rendering.
- Animated device icons.
- Particle background effects.
- Fullscreen screensaver window.
- Command line help support.
- Version reporting.
- Debug logging support.

### Cinnamon integration

- Cinnamon remains responsible for:
  - Screen locking.
  - Password authentication.
  - Unlock handling.

- Mint Device Screensaver provides only the visual screensaver experience.
- Cinnamon lock workflow verified.
- Normal Ctrl+Alt+L locking verified.

### Configuration

Completed:

- Configuration file support.
- Persistent user settings.
- Animation speed control.
- Background colour selection.
- Mouse movement exit behaviour.
- Reset to default settings.

Configuration location:

```text
~/.config/mint-device-screensaver/config.ini
