---
id: learning.zephyr-docs.usb.page-133
title: 旧版USB固件升级示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/dfu/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第133章\_旧版USB固件升级示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/dfu/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 133.1\_概述

此应用演示 Zephyr 提供的 USB 设备固件升级（Device Firmware Upgrade，DFU）类驱动。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 133.2\_运行要求

此项目需要 USB 设备驱动。Zephyr 提供的 USB DFU 类目前依赖 DFU 镜像管理器（DFU Image Manager）和分区布局（Partition Layout）；分区布局的详细说明见[闪存映射（Flash Map）](../storage/P001_Flash分区映射.md#flash-map-api)。目标片上系统（System on Chip，SoC）必须使用 MCUboot 作为第一级引导加载程序（Stage 1 Bootloader）。此示例构建为由 MCUboot 引导的应用。

> 原文注：本例显式启用 [`CONFIG_USB_DFU_ENABLE_UPLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_ENABLE_UPLOAD)。

## 133.3\_构建与测试

### 133.3.1\_构建并签名应用

可以按通常方式构建此示例，详见[构建应用](../application/P001_应用开发.md#build-an-application)，也可以使用常规烧录工具写入，但必须加载到 `SLOT-0` 的偏移位置。

包括此示例在内的应用镜像必须签名。设置 [`CONFIG_MCUBOOT_SIGNATURE_KEY_FILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_SIGNATURE_KEY_FILE) 后，构建系统可以完成签名。例如：

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/subsys/usb/legacy/dfu -d build-dfu -- \
-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"bootloader/mcuboot/root-rsa-2048.pem\"
```

按 [在 Zephyr 中使用 MCUboot](https://docs.mcuboot.com/readme-zephyr) 文档构建并烧录 MCUboot，然后构建、签名并把 USB DFU 示例烧录到 `SLOT-0` 的偏移位置。

再构建并签名第二个应用镜像，例如 [Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)，用作更新镜像。不要忘记启用 [`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)，详见 [MCUboot](../firmware_update/P002_设备固件升级.md#mcuboot)。例如：

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/hello_world -d build-hello_world -- \
-DCONFIG_BOOTLOADER_MCUBOOT=y '-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE="bootloader/mcuboot/root-rsa-2048.pem"'
```

> 译注：本页命令中的 `zephyr/samples/...` 和 `bootloader/mcuboot/...` 是官方工作区内的相对位置；与只含 `samples/...` 的其他示例不同，这里按包含 `zephyr` 与 `bootloader` 的工作区根目录解析。`build-dfu` 和 `build-hello_world` 分别隔离两个应用的构建目录。签名密钥和引导程序配置必须匹配，分区偏移应来自目标布局；不能将后文历史日志的 `0xc000` 当作所有开发板的固定偏移。

### 133.3.2\_测试

Linux 的 dfu-util 工具可用于备份或更新应用镜像。

使用以下命令备份 `SLOT-0` 镜像：

```shell
dfu-util --alt 0 --upload slot0_backup.bin
```

使用以下命令更新应用：

```shell
dfu-util --alt 1 --download build-hello_world/zephyr/zephyr.signed.bin
```

复位 SoC。MCUboot 会交换镜像并引导新应用，控制台显示如下输出：

```text
*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x3, copy_done=0x1, image_ok=0x1
I: Secondary image: magic=good, swap_type=0x2, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Swap type: test
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
Hello World! nrf52840dk
```

再次复位 SoC。MCUboot 应回退镜像并重新引导 USB DFU 示例，控制台显示如下输出：

```text
*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x2, copy_done=0x1, image_ok=0x3
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Swap type: revert
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
[00:00:00.005,920] <inf> main: This device supports USB DFU class.
```

> 译注：上传（Upload）表示设备向主机传出数据，下载（Download）表示主机向设备写入数据；因此 `--upload` 用于备份，`--download` 用于升级。上述日志保留原页的 `zephyr-v3.0.0` 构建标识、交换类型及偏移，不是本轮实际运行结果。测试升级（Test Upgrade）与永久升级（Permanent Upgrade）的行为不同，不能只凭首次成功启动就认定下一次复位仍会保留新镜像。

### 133.3.3\_永久下载与自动重启

以下配置符号可用于启用无需手动干预的下载流程：

- 启用 [`CONFIG_USB_DFU_PERMANENT_DOWNLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_PERMANENT_DOWNLOAD)，下载完成后将 `SLOT-1` 标记为永久镜像。
- 启用 [`CONFIG_USB_DFU_REBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_REBOOT)，下载完成后自动重启。

> 原文警告：启用 [`CONFIG_USB_DFU_PERMANENT_DOWNLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_PERMANENT_DOWNLOAD) 可能使设备无法正常使用（Bricked Device）。必须确保存在另一种固件下载途径，例如调试器或 MCUboot 的恢复模式（Recovery Mode）。

可以通过 `overlay-permanent-download.conf` 配置叠加文件同时启用这两个符号。例如：

```shell
west build -b nrf52840dk/nrf52840 zephyr/samples/subsys/usb/legacy/dfu -d build-dfu -- \
-DCONFIG_BOOTLOADER_MCUBOOT=y '-DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE="bootloader/mcuboot/root-rsa-2048.pem"' \
-DEXTRA_CONF_FILE=overlay-permanent-download.conf
```

下面是使用 dfu-util 下载时的控制台输出。请注意 `Swap type: perm`：

```text
*** Booting Zephyr OS build zephyr-v3.0.0-361-ge6900e2451d5  ***
[00:00:00.005,920] <inf> main: This device supports USB DFU class.

*** Booting Zephyr OS build zephyr-v3.0.0-360-gc0dd594d4d3d  ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x4, copy_done=0x1, image_ok=0x1
I: Secondary image: magic=good, swap_type=0x3, copy_done=0x3, image_ok=0x1
I: Boot source: none
I: Swap type: perm
I: Bootloader chainload address offset: 0xc000
I: Jumping to the first image slot
*** Booting Zephyr OS build zephyr-v3.0.0-361-gb987e6daa2f9  ***
Hello World! nrf52840dk
```

> 译注：当前 DFU 实现把 [`CONFIG_USB_DFU_PERMANENT_DOWNLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_PERMANENT_DOWNLOAD) 的启用状态传给 `boot_request_upgrade()`，而自动重启由 [`CONFIG_USB_DFU_REBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_REBOOT) 独立控制。两者不是同一个开关：自动重启本身不意味着永久接受镜像。本页保留原文的恢复要求，没有执行下载或复位测试。

## 133.4\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/dfu/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/dfu/src/main.c)、[samples/subsys/usb/legacy/dfu/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/dfu/prj.conf)、[samples/subsys/usb/legacy/dfu/overlay-permanent-download.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/dfu/overlay-permanent-download.conf)、[subsys/usb/device/class/dfu/usb_dfu.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/dfu/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-usb-dfu"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-testing"></a>
<a id="building-and-signing-the-application"></a>
<a id="testing"></a>
<a id="permanent-download-and-automatic-reboot"></a>
<a id="see-also"></a>

[上一章](P132_旧版USB串口控制台示例.md) · [返回大纲](大纲.md) · [下一章](P134_旧版USB示例目录.md)
