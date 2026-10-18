---
id: learning.zephyr-docs.kconfig-reference.page-435
title: "`subsys/usb`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第435章\_`subsys/usb`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `subsys/usb` 的 78 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USBD_VREQ_SUPPORT"></a>

## 435.1 `CONFIG_USBD_VREQ_SUPPORT`

**提示（Prompt）**：USB 设备供应商请求（Vendor request）支持

**说明（Help）**

允许应用注册处理程序，处理接收者（Recipient）为设备的供应商请求（Vendor request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK_NEXT)。

<a id="CONFIG_USBH_HUB_CLASS"></a>

## 435.2 `CONFIG_USBH_HUB_CLASS`

**提示（Prompt）**：USB 主机集线器类驱动（Host Hub Class Driver）

**说明（Help）**

启用 USB 主机集线器类驱动（Host Hub Class driver）支持，允许连接 USB 集线器（Hub）并管理下游设备（Downstream device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_ENUM_RETRY_DELAY_MS"></a>

## 435.3 `CONFIG_USBH_HUB_ENUM_RETRY_DELAY_MS`

**提示（Prompt）**：枚举重试延迟（Enumeration retry delay，毫秒）

**说明（Help）**

设备枚举（Enumeration）失败后，再次尝试前的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[100, 3000]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_ERROR_RECOVERY_DELAY_MS"></a>

## 435.4 `CONFIG_USBH_HUB_ERROR_RECOVERY_DELAY_MS`

**提示（Prompt）**：错误恢复延迟（Error recovery delay，毫秒）

**说明（Help）**

严重错误后重试前的延迟。较长延迟有助于避免大量重试淹没总线。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[500, 5000]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_INIT_PRIO"></a>

## 435.5 `CONFIG_USBH_HUB_INIT_PRIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

USB 主机集线器类（Host Hub Class）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
89
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_INSTANCES_COUNT"></a>

## 435.6 `CONFIG_USBH_HUB_INSTANCES_COUNT`

**提示（Prompt）**：`USBH_HUB` 实例（Instance）数量

**说明（Help）**

此 USB 类实现的实例（Instance）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`subsys/usb/common/Kconfig.template.instances_count:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/common/Kconfig.template.instances_count#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_MAX_LEVELS"></a>

## 435.7 `CONFIG_USBH_HUB_MAX_LEVELS`

**提示（Prompt）**：集线器链最大深度（Maximum hub chain depth）

**说明（Help）**

主机与任意设备之间一条通信路径上，允许存在的非根集线器（Non-root hub）的最大数量。USB 规范允许每条路径最多五个非根集线器，因此最深路径可包含 5 个集线器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_PORT_RESET_DELAY_MS"></a>

## 435.8 `CONFIG_USBH_HUB_PORT_RESET_DELAY_MS`

**提示（Prompt）**：集线器端口复位信号持续时间（Port reset signalling delay，毫秒）

**说明（Help）**

驱动端口复位信号（Port reset signalling）的持续时间。原文说明 USB 规范要求 10～20 毫秒，默认使用 20 毫秒，以提高最坏情况下的兼容性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[10, 50]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_PORT_RESET_TIMES"></a>

## 435.9 `CONFIG_USBH_HUB_PORT_RESET_TIMES`

**提示（Prompt）**：集线器端口复位重试次数（Reset retry count）

**说明（Help）**

放弃前尝试端口复位（Port reset）的最大重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_HUB_STACK_SIZE"></a>

## 435.10 `CONFIG_USBH_HUB_STACK_SIZE`

**提示（Prompt）**：USB 主机集线器工作队列栈大小（Hub workqueue stack size）

**说明（Help）**

共享的 USB 主机集线器工作队列（Workqueue）线程栈大小。该线程执行集线器状态处理和下游设备枚举，包括类驱动探测（Class driver probe），因此需要足够栈余量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.hub:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.hub#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_INIT_PRIO"></a>

## 435.11 `CONFIG_USBH_INIT_PRIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

USB 主机线程的初始化优先级（Initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_MAX_UHC_MSG"></a>

## 435.12 `CONFIG_USBH_MAX_UHC_MSG`

**提示（Prompt）**：USB 主机控制器（UHC）事件的最大数量

**说明（Help）**

可排队的 USB 主机控制器（USB Host Controller，UHC）事件的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_SHELL"></a>

## 435.13 `CONFIG_USBH_SHELL`

**提示（Prompt）**：USB 主机命令行（Host shell）

**说明（Help）**

USB 主机功能的命令行命令（Shell command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_USB_HOST_STACK
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_STACK_SIZE"></a>

## 435.14 `CONFIG_USBH_STACK_SIZE`

**提示（Prompt）**：USB 主机协议栈线程栈大小（Thread stack size）

**说明（Help）**

USB 主机协议栈线程的栈大小（Stack size），单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_USB_DEVICE_HEAP"></a>

## 435.15 `CONFIG_USBH_USB_DEVICE_HEAP`

**提示（Prompt）**：用于缓存设备描述符（Device descriptor）的内存

**说明（Help）**

用于缓存设备描述符（Device descriptor）的内存大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[256, 16384]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_USB_DEVICE_MAX"></a>

## 435.16 `CONFIG_USBH_USB_DEVICE_MAX`

**提示（Prompt）**：支持的 USB 设备最大数量

**说明（Help）**

全部控制器合计支持的 USB 设备最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 127]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_UVC_INSTANCES_COUNT"></a>

## 435.17 `CONFIG_USBH_UVC_INSTANCES_COUNT`

**提示（Prompt）**：`USBH_UVC` 实例（Instance）数量

**说明（Help）**

此 USB 类实现的实例（Instance）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/usb/common/Kconfig.template.instances_count:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/common/Kconfig.template.instances_count#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_CLASS"></a>

## 435.18 `CONFIG_USBH_VIDEO_CLASS`

**提示（Prompt）**：USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**说明（Help）**

USB 主机视频类（USB Host Video Class，UVC）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_HOST_STACK
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS"></a>

## 435.19 `CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS`

**提示（Prompt）**：启动视频流时发起的并发 USB 传输数量

**说明（Help）**

视频流开始时发起的并发 USB 等时传输（Isochronous Transfer）数量。较大的值可提高吞吐量，但会消耗更多资源。较小的值（1～2）适合低帧率，较大的值（4～8）适合高帧率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_INSTANCES_COUNT"></a>

## 435.20 `CONFIG_USBH_VIDEO_INSTANCES_COUNT`

**提示（Prompt）**：主机 UVC 实例数量

**说明（Help）**

此 USB 类的实例数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_MAX_CAPS"></a>

## 435.21 `CONFIG_USBH_VIDEO_MAX_CAPS`

**提示（Prompt）**：格式能力条目的最大数量

**说明（Help）**

视频格式能力的最大数量

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 512]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_MAX_FORMATS"></a>

## 435.22 `CONFIG_USBH_VIDEO_MAX_FORMATS`

**提示（Prompt）**：格式描述符（Format descriptor）的最大数量

**说明（Help）**

格式描述符表（Format Descriptor Table）在运行时生成。此选项在构建时预留存储空间，以便生成足够的描述符。默认值旨在兼顾多数设备所需的描述符数量与内存占用。此值是每种格式类型（如 MJPEG、未压缩格式）的最大数量，而非所有格式的总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_MAX_FRMIVAL"></a>

## 435.23 `CONFIG_USBH_VIDEO_MAX_FRMIVAL`

**提示（Prompt）**：每个描述符支持的视频帧间隔最大数量

**说明（Help）**

帧描述符（Frame Descriptor）中列出的帧间隔（Frame Interval）的最大数量。默认值是为适应多数情况而酌情选择的。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_MAX_STREAM_INTERFACE_ALT"></a>

## 435.24 `CONFIG_USBH_VIDEO_MAX_STREAM_INTERFACE_ALT`

**提示（Prompt）**：USB 视频流接口的最大数量

**说明（Help）**

视频流接口的备用设置（Alternate Setting）的最大数量。默认值是为适应多数情况且避免占用过多 RAM 而酌情选择的。译注：此帮助正文说明的是备用设置数量，提示标题写的是视频流接口数量，两者均保留原文含义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBH_VIDEO_NUM_BUFS"></a>

## 435.25 `CONFIG_USBH_VIDEO_NUM_BUFS`

**提示（Prompt）**：USB 视频类（UVC）可分配的最大缓冲区数量

**说明（Help）**

控制 USB 视频类（UVC）可同时分配的缓冲区数量。默认值在足够的并发缓冲区与适度内存占用之间折中。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/usb/host/class/Kconfig.uvc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/class/Kconfig.uvc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBH_VIDEO_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBIP"></a>

## 435.26 `CONFIG_USBIP`

**提示（Prompt）**：通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**说明（Help）**

实验性的 USB USBIP 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_NET_IPV4 && CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_USB_HOST_STACK
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_USBIP_BUF_COUNT"></a>

## 435.27 `CONFIG_USBIP_BUF_COUNT`

**提示（Prompt）**：USBIP 池中的缓冲区数量

**说明（Help）**

池中的 USBIP 请求缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBIP_BUF_POOL_SIZE"></a>

## 435.28 `CONFIG_USBIP_BUF_POOL_SIZE`

**提示（Prompt）**：USBIP 缓冲区可用内存

**说明（Help）**

USBIP 缓冲区可用的内存总量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
16777216 if CONFIG_BOARD_NATIVE_SIM
65536
```

**取值范围（Ranges）**

```text
[4096, 4294967295]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)、[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NATIVE_SIM`。

<a id="CONFIG_USBIP_DEVICES_COUNT"></a>

## 435.29 `CONFIG_USBIP_DEVICES_COUNT`

**提示（Prompt）**：可导出的设备数量

**说明（Help）**

可导出的设备数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBIP_SERVICE_PORT"></a>

## 435.30 `CONFIG_USBIP_SERVICE_PORT`

**提示（Prompt）**：USBIP 服务的端口号

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
3240
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBIP_SUBMIT_BACKLOG_COUNT"></a>

## 435.31 `CONFIG_USBIP_SUBMIT_BACKLOG_COUNT`

**提示（Prompt）**：积压队列中的提交命令数量

**说明（Help）**

积压队列（Backlog）中可存放的提交命令（Submit Command）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
48
```

**取值范围（Ranges）**

```text
[32, 128]
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USBIP_THREAD_STACK_SIZE"></a>

## 435.32 `CONFIG_USBIP_THREAD_STACK_SIZE`

**提示（Prompt）**：USBIP 线程栈大小

**说明（Help）**

USBIP 线程栈大小，以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig.usbip:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig.usbip#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_USBIP`](P435_subsys_usb_配置项参考_2.md#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_HOST_STACK)。

<a id="CONFIG_USB_CDC_ACM"></a>

## 435.33 `CONFIG_USB_CDC_ACM`

**提示（Prompt）**：USB 通信设备类抽象控制模型支持（CDC ACM Class）

**说明（Help）**

USB 通信设备类抽象控制模型（CDC ACM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && DT_HAS_ZEPHYR_CDC_ACM_UART_ENABLED && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USB_COMPOSITE_DEVICE
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_COMPOSITE_DEVICE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_COMPOSITE_DEVICE)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_USB_CDC_ACM_RINGBUF_SIZE"></a>

## 435.34 `CONFIG_USB_CDC_ACM_RINGBUF_SIZE`

**提示（Prompt）**：USB CDC ACM 环形缓冲区（Ring Buffer）大小

**说明（Help）**

USB CDC ACM 环形缓冲区（Ring Buffer）大小

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.cdc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.cdc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_COMPOSITE_DEVICE"></a>

## 435.35 `CONFIG_USB_COMPOSITE_DEVICE`

**提示（Prompt）**：使用接口关联描述符的代码三元组

**说明（Help）**

此选项修改设备描述符中的代码三元组（Code Triple），以表明其中某个功能具有两个或更多接口，并使用接口关联描述符（Interface Association Descriptor，IAD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**被选择（Selected by）**

```text
CONFIG_USB_CDC_ACM
CONFIG_USB_DEVICE_NETWORK_ECM
CONFIG_USB_DEVICE_NETWORK_RNDIS
CONFIG_USB_DEVICE_AUDIO
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_NETWORK_ECM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_ECM)、[`CONFIG_USB_DEVICE_NETWORK_RNDIS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_RNDIS)、[`CONFIG_USB_DEVICE_AUDIO`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_AUDIO)。

<a id="CONFIG_USB_CONFIGURATION_STRING_DESC"></a>

## 435.36 `CONFIG_USB_CONFIGURATION_STRING_DESC`

**提示（Prompt）**：USB 配置字符串描述符

**说明（Help）**

描述默认配置的字符串描述符（String Descriptor）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CONFIGURATION_STRING_DESC_ENABLE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"Default Configuration"
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 配置字符串描述符支持

**配置项引用（Symbol References）**：[`CONFIG_USB_CONFIGURATION_STRING_DESC_ENABLE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CONFIGURATION_STRING_DESC_ENABLE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_CONFIGURATION_STRING_DESC_ENABLE"></a>

## 435.37 `CONFIG_USB_CONFIGURATION_STRING_DESC_ENABLE`

**提示（Prompt）**：USB 配置字符串描述符支持

**说明（Help）**

启用描述默认配置的字符串描述符。由于只有一个配置，此字符串描述符可能无法提供多少有用信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_AUDIO"></a>

## 435.38 `CONFIG_USB_DEVICE_AUDIO`

**提示（Prompt）**：USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】

**说明（Help）**

USB 音频设备类（USB Audio Device Class）驱动。Zephyr USB 音频类仍属于实验性功能，实现尚不完整。设备通过设备树覆盖文件（Devicetree Overlay）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_USB_COMPOSITE_DEVICE
```

**定义位置（Location）**：[`subsys/usb/device/class/audio/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/audio/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_USB_COMPOSITE_DEVICE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_COMPOSITE_DEVICE)。

<a id="CONFIG_USB_DEVICE_BLUETOOTH"></a>

## 435.39 `CONFIG_USB_DEVICE_BLUETOOTH`

**提示（Prompt）**：USB 蓝牙设备类（USB Bluetooth Device Class）支持

**说明（Help）**

USB 蓝牙设备类（USB Bluetooth Device Class）支持

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_BT
CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.bt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.bt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)。

<a id="CONFIG_USB_DEVICE_BOS"></a>

## 435.40 `CONFIG_USB_DEVICE_BOS`

**提示（Prompt）**：USB 二进制设备对象存储（Binary Device Object Store，BOS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_DFU_PID"></a>

## 435.41 `CONFIG_USB_DEVICE_DFU_PID`

**提示（Prompt）**：USB DFU 产品 ID

**说明（Help）**

设备固件升级（Device Firmware Upgrade，DFU）模式下的 USB 设备产品 ID。必须由供应商配置。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
0xFFFF
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_HID"></a>

## 435.42 `CONFIG_USB_DEVICE_HID`

**提示（Prompt）**：USB 人机接口设备支持（Human Interface Device）

**说明（Help）**

启用 USB 人机接口设备（Human Interface Device，HID）支持。默认设备名为 `HID_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_INITIALIZE_AT_BOOT"></a>

## 435.43 `CONFIG_USB_DEVICE_INITIALIZE_AT_BOOT`

**提示（Prompt）**：在启动时初始化 USB 设备支持

**说明（Help）**

将 CDC ACM UART 用作控制台（Console）、命令行（Shell）或日志（Logging）的后端（Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_MANUFACTURER"></a>

## 435.44 `CONFIG_USB_DEVICE_MANUFACTURER`

**提示（Prompt）**：USB 制造商名称

**说明（Help）**

USB 设备制造商字符串（Manufacturer String）。必须由供应商配置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"ZEPHYR"
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_NETWORK_ECM"></a>

## 435.45 `CONFIG_USB_DEVICE_NETWORK_ECM`

**提示（Prompt）**：USB 以太网控制模型（Ethernet Control Model，ECM）网络设备

**说明（Help）**

以太网控制模型（Ethernet Control Model，ECM）属于 USB 实现者论坛（USB-IF）规定的通信设备类（Communications Device Class，CDC）USB 协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_USB_DEVICE_NETWORK
CONFIG_USB_COMPOSITE_DEVICE
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_USB_COMPOSITE_DEVICE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_COMPOSITE_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_USB_DEVICE_NETWORK_ECM_MAC"></a>

## 435.46 `CONFIG_USB_DEVICE_NETWORK_ECM_MAC`

**提示（Prompt）**：USB ECM 主机操作系统 MAC 地址

**说明（Help）**

主机操作系统的 MAC 地址字符串。此 MAC 地址将分配给主机操作系统中创建的网络设备。默认 MAC 使用 RFC 7042 中用于文档示例的地址值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_NETWORK_ECM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"00005E005301"
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_ECM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_ECM)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_NETWORK_EEM"></a>

## 435.47 `CONFIG_USB_DEVICE_NETWORK_EEM`

**提示（Prompt）**：USB 以太网仿真模型（Ethernet Emulation Model，EEM）网络设备

**说明（Help）**

以太网仿真模型（Ethernet Emulation Model，EEM）属于通信设备类（Communications Device Class，CDC）USB 协议，可封装以太网帧以通过 USB 传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_USB_DEVICE_NETWORK
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_USB_DEVICE_NETWORK_RNDIS"></a>

## 435.48 `CONFIG_USB_DEVICE_NETWORK_RNDIS`

**提示（Prompt）**：USB 远程 NDIS（Remote NDIS，RNDIS）网络设备

**说明（Help）**

远程 NDIS（Remote NDIS，RNDIS）是一种常用的 Microsoft 厂商协议，其规范可从 Microsoft 网站获取。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_USB_DEVICE_NETWORK
CONFIG_USB_COMPOSITE_DEVICE
```

**定义位置（Location）**：[`subsys/usb/device/class/netusb/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/netusb/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_USB_COMPOSITE_DEVICE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_COMPOSITE_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_USB_DEVICE_OS_DESC"></a>

## 435.49 `CONFIG_USB_DEVICE_OS_DESC`

**提示（Prompt）**：Microsoft 操作系统描述符（MS OS Descriptors）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_PID"></a>

## 435.50 `CONFIG_USB_DEVICE_PID`

**提示（Prompt）**：USB 产品 ID

**说明（Help）**

USB 设备产品 ID。必须由供应商配置。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
0x0100
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_PRODUCT"></a>

## 435.51 `CONFIG_USB_DEVICE_PRODUCT`

**提示（Prompt）**：USB 产品名称

**说明（Help）**

USB 设备产品字符串（Product String）。必须由供应商配置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"USB-DEV"
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_SN"></a>

## 435.52 `CONFIG_USB_DEVICE_SN`

**提示（Prompt）**：USB 设备序列号字符串

**说明（Help）**

USB 设备序列号字符串（Serial Number String）的占位值。序列号字符串将从硬件信息驱动（Hardware Information Driver，HWINFO）获取。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"0123456789ABCDEF"
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DEVICE_SOF"></a>

## 435.53 `CONFIG_USB_DEVICE_SOF`

**提示（Prompt）**：在事件中处理帧起始（Start of Frame，SOF）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y if CONFIG_USB_DEVICE_AUDIO && CONFIG_NRF_USBD_COMMON
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_AUDIO`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_AUDIO)、[`CONFIG_NRF_USBD_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_NRF_USBD_COMMON)。

<a id="CONFIG_USB_DEVICE_STACK"></a>

## 435.54 `CONFIG_USB_DEVICE_STACK`

**提示（Prompt）**：USB 设备支持（Device Support）【已弃用 DEPRECATED】

**说明（Help）**

启用 USB 设备协议栈（USB Device Stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_USB_DEVICE_DRIVER
CONFIG_HWINFO
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_USB_DEVICE_STACK_NEXT"></a>

## 435.55 `CONFIG_USB_DEVICE_STACK_NEXT`

**提示（Prompt）**：新 USB 设备协议栈（device stack）

**说明（Help）**

新的 USB 设备协议栈（USB Device Stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_UDC_DRIVER
```

**弱选择（Implies）**

```text
CONFIG_HWINFO
```

**定义位置（Location）**：[`subsys/usb/device_next/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)。

<a id="CONFIG_USB_DEVICE_VID"></a>

## 435.56 `CONFIG_USB_DEVICE_VID`

**提示（Prompt）**：USB 供应商 ID

**说明（Help）**

USB 设备供应商 ID。必须由供应商配置。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
0x2FE3
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DFU_CLASS"></a>

## 435.57 `CONFIG_USB_DFU_CLASS`

**提示（Prompt）**：USB DFU 类驱动（Class Driver）

**说明（Help）**

USB DFU 类驱动（Class Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IMG_MANAGER && CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_POLL
CONFIG_IMG_ERASE_PROGRESSIVELY if CONFIG_SOC_FLASH_NRF || CONFIG_FLASH_MCUX_FLEXSPI_NOR
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_IMG_ERASE_PROGRESSIVELY`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ERASE_PROGRESSIVELY)、[`CONFIG_SOC_FLASH_NRF`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)。

<a id="CONFIG_USB_DFU_DEFAULT_POLLTIMEOUT"></a>

## 435.58 `CONFIG_USB_DFU_DEFAULT_POLLTIMEOUT`

**提示（Prompt）**：`bwPollTimeout` 的默认值

**说明（Help）**

`bwPollTimeout` 的默认值，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DFU_ENABLE_UPLOAD"></a>

## 435.59 `CONFIG_USB_DFU_ENABLE_UPLOAD`

**提示（Prompt）**：将固件上传到主机

**说明（Help）**

启用此选项后，可将固件镜像上传到主机。请注意，上传能力可能带来安全风险：即使已启用镜像加密，可执行镜像也始终以解密后的形式提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DFU_PERMANENT_DOWNLOAD"></a>

## 435.60 `CONFIG_USB_DFU_PERMANENT_DOWNLOAD`

**提示（Prompt）**：下载后将槽位 1 标记为永久镜像

**说明（Help）**

启用后，写入槽位 1（Slot 1）的镜像将被标记为永久镜像（Permanent）。警告：这会绕过 MCUboot 的试运行与确认机制（Test-Confirm Mechanism）！下载错误的镜像会导致设备变砖。请确保存在某种恢复机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_DFU_REBOOT"></a>

## 435.61 `CONFIG_USB_DFU_REBOOT`

**提示（Prompt）**：下载后重启

**说明（Help）**

启用后，设备将在下载完成后自动重启，以便引导加载程序（Bootloader）交换镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_REBOOT
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)。

<a id="CONFIG_USB_DFU_WILL_DETACH"></a>

## 435.62 `CONFIG_USB_DFU_WILL_DETACH`

**提示（Prompt）**：在 DFU 分离时生成分离与重新连接序列

**说明（Help）**

启用此选项后，设备负责在收到 `DFU_DETACH` 请求后自行从总线分离。对于无法发出 USB 复位的主机驱动，应选择此选项以确保兼容性。若不启用，在 Windows 上使用 WinUSB 驱动时 DFU 将失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DFU_CLASS && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device/class/dfu/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/dfu/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB DFU 类驱动（Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_USB_DFU_CLASS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DFU_CLASS)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HID_BOOT_PROTOCOL"></a>

## 435.63 `CONFIG_USB_HID_BOOT_PROTOCOL`

**提示（Prompt）**：USB HID 引导协议（Boot Protocol）处理

**说明（Help）**

将 `bInterfaceSubClass` 设置为 1，并启用 `Set_Protocol` 和 `Get_Protocol` 请求处理。更多信息参见《人机接口设备类定义》（Device Class Definition for Human Interface Devices）1.11 版第 4.2 章。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HID_DEVICE_COUNT"></a>

## 435.64 `CONFIG_USB_HID_DEVICE_COUNT`

**提示（Prompt）**：`USB_HID` 设备数量

**说明（Help）**

此 USB 设备类的实例数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.template.composite_device_number:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.template.composite_device_number#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HID_DEVICE_NAME"></a>

## 435.65 `CONFIG_USB_HID_DEVICE_NAME`

**提示（Prompt）**：USB HID 设备名称模板

**说明（Help）**

HID 设备的名称模板。第一个设备的名称为 `$(USB_HID_DEVICE_NAME)_0`，其余依此类推。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
"HID"
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HID_POLL_INTERVAL_MS"></a>

## 435.66 `CONFIG_USB_HID_POLL_INTERVAL_MS`

**提示（Prompt）**：轮询间隔（Polling Interval）

**说明（Help）**

USB HID 设备选择的轮询间隔，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
9
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HID_REPORTS"></a>

## 435.67 `CONFIG_USB_HID_REPORTS`

**提示（Prompt）**：实例中 HID 空闲报告的数量

**说明（Help）**

仅当应用必须支持 USB HID 空闲速率（Idle Rate）和设置／获取空闲参数请求（Set/Get Idle Requests）时，才需要此配置。应用可使用报告 ID（Report ID）标识报告描述符及报告本身中的数据字段。此配置值应对应输入报告 ID（Input Report ID）的数量；不支持报告 ID 存在间断或起始偏移。如果未使用报告 ID，但必须支持空闲速率，则将此配置值设为 1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/usb/device/class/hid/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/hid/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_HID`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_HOST_STACK"></a>

## 435.68 `CONFIG_USB_HOST_STACK`

**提示（Prompt）**：USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**说明（Help）**

新的实验性 USB 主机协议栈（USB Host Stack）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_UHC_DRIVER
```

**定义位置（Location）**：[`subsys/usb/host/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/host/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)。

<a id="CONFIG_USB_MASS_STORAGE"></a>

## 435.69 `CONFIG_USB_MASS_STORAGE`

**提示（Prompt）**：USB 大容量存储设备类支持（Mass Storage Device Class）

**说明（Help）**

USB 大容量存储设备类（Mass Storage Device Class）支持

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**主动选择（Selects）**

```text
CONFIG_DISK_ACCESS
```

**定义位置（Location）**：[`subsys/usb/device/class/Kconfig.msc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/class/Kconfig.msc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_DISK_ACCESS`](P340_subsys_disk_配置项参考.md#CONFIG_DISK_ACCESS)。

<a id="CONFIG_USB_MAX_ALT_SETTING"></a>

## 435.70 `CONFIG_USB_MAX_ALT_SETTING`

**提示（Prompt）**：存放备用设置的数组大小

**说明（Help）**

存放备用设置（Alternate Settings）的数组大小。不应小于接口数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 16]
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_MAX_NUM_TRANSFERS"></a>

## 435.71 `CONFIG_USB_MAX_NUM_TRANSFERS`

**提示（Prompt）**：设置 USB 传输数据缓冲区数量

**说明（Help）**

分配用于并行传输的缓冲区。应根据 USB 设备数量增加此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_MAX_POWER"></a>

## 435.72 `CONFIG_USB_MAX_POWER`

**提示（Prompt）**：设置 `bMaxPower` 值

**说明（Help）**

设置标准配置描述符（Standard Configuration Descriptor）中的 `bMaxPower` 值，对应电流为所填值乘以 2 mA。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 250]
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_NUMOF_EP_WRITE_RETRIES"></a>

## 435.73 `CONFIG_USB_NUMOF_EP_WRITE_RETRIES`

**提示（Prompt）**：端点写入重试次数

**说明（Help）**

端点（Endpoint）写入重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_REQUEST_BUFFER_SIZE"></a>

## 435.74 `CONFIG_USB_REQUEST_BUFFER_SIZE`

**提示（Prompt）**：设置标准、类及厂商请求处理程序的缓冲区大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
256 if CONFIG_USB_DEVICE_NETWORK_RNDIS
266 if CONFIG_USB_DEVICE_BLUETOOTH && CONFIG_USB_DEVICE_BLUETOOTH_BIG_BUF
128
```

**取值范围（Ranges）**

```text
[64, 512] if CONFIG_USB_DEVICE_NETWORK_RNDIS
[8, 65536]
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_NETWORK_RNDIS`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_NETWORK_RNDIS)、[`CONFIG_USB_DEVICE_BLUETOOTH`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_BLUETOOTH)、[`CONFIG_USB_DEVICE_BLUETOOTH_BIG_BUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_BLUETOOTH_BIG_BUF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_BLUETOOTH_BIG_BUF`。

<a id="CONFIG_USB_SELF_POWERED"></a>

## 435.75 `CONFIG_USB_SELF_POWERED`

**提示（Prompt）**：设置自供电（Self-powered）特性

**说明（Help）**

设置 `bmAttributes` 中的自供电（Self-powered）特性，以表明 USB 设备由自身电源供电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)。

<a id="CONFIG_USB_WORKQUEUE"></a>

## 435.76 `CONFIG_USB_WORKQUEUE`

**提示（Prompt）**：在 USB 子系统中使用专用工作队列

**说明（Help）**

此选项提供一个专用工作队列（Dedicated Work Queue），供 USB 子系统发起的所有卸载操作使用。它可防止以下死锁：系统工作队列上的任务意外发起会阻塞的操作，例如通过 CDC-ACM 发送 UART 数据，导致系统工作队列无法继续处理能够解除该任务阻塞的 USB 工作。不启用此选项时，所有 USB 卸载传输均使用系统工作队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
y if CONFIG_USB_CDC_ACM
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_CDC_ACM`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_CDC_ACM)。

<a id="CONFIG_USB_WORKQUEUE_PRIORITY"></a>

## 435.77 `CONFIG_USB_WORKQUEUE_PRIORITY`

**提示（Prompt）**：USB 工作队列优先级

**说明（Help）**

默认情况下，USB 工作队列采用最低的协作式优先级（Cooperative Priority）。原文据此说明：工作处理函数一旦开始执行，在完成前不会被其他任何线程抢占。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_WORKQUEUE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
-2 if CONFIG_COOP_ENABLED && !CONFIG_PREEMPT_ENABLED
0 if !CONFIG_COOP_ENABLED
-1
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → 在 USB 子系统中使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_USB_WORKQUEUE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_WORKQUEUE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_COOP_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COOP_ENABLED)、[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_COOP_ENABLED`、`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_USB_WORKQUEUE_STACK_SIZE"></a>

## 435.78 `CONFIG_USB_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：USB 工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_WORKQUEUE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
4096 if CONFIG_COVERAGE_GCOV
1024
```

**定义位置（Location）**：[`subsys/usb/device/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → 在 USB 子系统中使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_USB_WORKQUEUE`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_WORKQUEUE)、[`CONFIG_USB_DEVICE_STACK`](P435_subsys_usb_配置项参考_2.md#CONFIG_USB_DEVICE_STACK)、[`CONFIG_COVERAGE_GCOV`](P431_subsys_testsuite_配置项参考.md#CONFIG_COVERAGE_GCOV)。

<!-- kconfig-navigation -->

[上一章](P434_subsys_usb_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P436_subsys_video_配置项参考.md)
