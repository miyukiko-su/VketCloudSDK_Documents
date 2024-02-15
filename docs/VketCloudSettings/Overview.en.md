# Vket Cloud Settings - Overview

![Overview_2](img/Overview_2.jpg)

Vket Cloud Settings is a suite of objects introduced in SDKVer12.0, which handles world settings in each category.<br>
The settings are a refinement and reorganization of HEO components such as [HEOWorldSetting](../HEOComponents/HEOWorldSetting.md), [HEOPlayer](../HEOComponents/HEOPlayer.md), and [HEODespawnHeight](../HEOComponents/HEODespawnHeight.md), aimed for better convenience and practicalness.

!!! note "Migrating settings on updating SDK version"
    When updating a world made in pre-SDK Ver12.0 environments to Ver12.0, the settings in [HEOWorldSetting](../HEOComponents/HEOWorldSetting.md), [HEOPlayer](../HEOComponents/HEOPlayer.md), and [HEODespawnHeight](../HEOComponents/HEODespawnHeight.md) will be migrated to each Settings objects automatically.

## How to use VketCloudSettings

VketCloudSettings and each Settings object can be generated by right-clicking on the Hierarchy and selecting **"Add essential objects for VketCloud"** on the menu.

![Overview_1](img/Overview_1.jpg)

On the "VketCloudSettings" object, the Inspector shows two modes: "Base" and "Advanced".

The Base mode is selected initially, which generates the fundamental three Settings objects to be edited.

For creators seeking further modification, the Advanced mode can be selected to generate Settings objects such as Rendering, Avatar, etc.

![Overview_2](img/Overview_2.jpg)

## Setting Modes

### Base

![Overview_3](img/Overview_3.jpg)

On Base mode, three Settings objects: [BasicSettings](./BasicSettings.md), [PlayerSettings](./PlayerSettings.md), and [DespawnHeightSettings](./DespawnHeightSettings.md) will be generated.

For each Settings' detail, refer to the pages below.

- [BasicSettings](./BasicSettings.md)

- [PlayerSettings](./PlayerSettings.md)

- [DespawnHeightSettings](./DespawnHeightSettings.md)

### Advanced

![Overview_4](img/Overview_4.jpg)

On Advanced mode, four Settings objects: [CameraSettings](./CameraSettings.md), [RenderingSettings](./RenderingSettings.md), [AvatarSettings](./AvatarSettings.md), and [MyAvatarSettings](./MyAvatarSettings.md) will be generated alongside Base objects.

For each Settings' detail, refer to the pages below.

- [Camera Settings](./CameraSettings.md)
  
- [Rendering Settings](./RenderingSettings.md)

- [Avatar Settings](./AvatarSettings.md)

- [MyAvatar Settings](./MyAvatarSettings.md)