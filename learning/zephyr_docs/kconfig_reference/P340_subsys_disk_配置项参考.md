---
id: learning.zephyr-docs.kconfig-reference.page-340
title: "`subsys/disk`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第340章\_`subsys/disk`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/disk` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DISK_ACCESS"></a>

## 340.1 `CONFIG_DISK_ACCESS`

**提示（Prompt）**：磁盘接口（Disk Interface）

**说明（Help）**

通过受支持的介质后端（media backend）启用磁盘访问，例如闪存（FLASH）或 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DISK_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_FAT_FILESYSTEM_ELM
CONFIG_USB_MASS_STORAGE
CONFIG_USBD_MSC_CLASS
```

**定义位置（Location）**：[`subsys/disk/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/disk/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_FAT_FILESYSTEM_ELM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_USB_MASS_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USBD_MSC_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_MSC_CLASS)。

<!-- kconfig-navigation -->

[上一章](P339_subsys_dfu_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P341_subsys_dsp_配置项参考.md)
