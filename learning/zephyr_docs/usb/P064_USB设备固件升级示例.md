---
id: learning.zephyr-docs.usb.page-64
title: USB设备固件升级示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/dfu/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_USB设备固件升级示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/dfu/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 64.1\_概述（Overview）

本示例演示使用新版实验性USB设备栈（USB Device Stack）实现USB设备固件升级（Device Firmware Upgrade，DFU）。

## 64.2\_前提条件（Requirements）

本示例需要实验性USB设备驱动，即支持USB设备控制器（USB Device Controller，UDC）API的驱动，并使用 [磁盘访问（Disk Access）](../storage/P008_磁盘访问.md#disk-access-api) 和RAM磁盘（RAM Disk）下载／上传镜像。

> 译注：DFU命令中的下载（Download）是主机向设备传输，上传（Upload）是设备向主机传输。RAM磁盘只用于演示数据传输，掉电后不保留，也不会仅因写入数据就成为可启动固件。

## 64.3\_构建与运行（Building and Running）

本示例支持多种开发板，下面以reel board为例：

> 译注：以下构建和烧录命令在读者的Zephyr源码根目录执行，终端可用Bash；前提是已准备Zephyr依赖、目标工具链、支持的开发板及烧录工具。成功构建后才进行烧录。后续 [`dfu-util`](https://dfu-util.sourceforge.net/) 命令在连接设备的主机终端运行，需预先安装该工具并具备USB访问权限。设备不出现时先检查固件、USB设备接口和当前模式，不重复执行构建以代替枚举排错。

```bash
west build -b reel_board samples/subsys/usb/dfu
west flash
```

可使用 [`dfu-util`](https://dfu-util.sourceforge.net/) 下载或上传镜像。USB DFU有运行时模式（Runtime Mode）和DFU模式；此示例启动后处于运行时模式。只切换到DFU模式而不上传或下载时，执行：

```bash
dfu-util --detach
```

使用下列命令将 `ramdisk0` 镜像上传到主机：

```bash
dfu-util --alt 0 --upload ramdisk0_backup.bin
```

使用下列命令将 `ramdisk0` 镜像下载到设备：

```bash
dfu-util --alt 0 --download ramdisk0_backup.bin
```

> 译注（源码跟踪）：当前示例在切换模式时停用并关闭运行时USB上下文，再建立DFU上下文、注册 `dfu_dfu` 类并启用。`--alt 0` 选择接口的备用设置（Alternate Setting）；`ramdisk0` 是DFU镜像名称，底层磁盘名为 `image0`，覆盖文件使用32个512字节扇区，即16 KiB。主机上的 `ramdisk0_backup.bin` 则是相对当前终端目录解析的文件名，这三个名字用途不同。

### 64.3.1\_启用Flash后端构建（Building with Flash Backend Enabled）

USB DFU设备支持内置Flash后端（Flash Backend）。它使用 [Flash镜像（Flash Image）](../firmware_update/P002_设备固件升级.md#flash-img-api) 和 [Flash映射（Flash Map）](../storage/P001_Flash分区映射.md#flash-map-api) 读写Flash镜像，实现与之前的USB DFU设备示例相似。

设置 `CONFIG_APP_USB_DFU_USE_FLASH_BACKEND` 可启用Flash后端。进入DFU模式后会多出一个用于上传／下载SLOT-1镜像的接口。

> 译注：当前示例Kconfig选择Flash、Flash Map、Stream Flash和镜像管理相关依赖，启用SLOT-1并默认停用SLOT-0后端；它不是“挂载前擦除文件系统”的选项，原Kconfig帮助文字有遗留描述。类的Flash后端还要求对应分区存在，不能仅凭开关开启就假定板上已具备正确的槽位布局。

也可以结合MCUboot引导加载程序（Bootloader）尝试本示例。下列命令通过 [系统构建（Sysbuild）](../sysbuild/P001_系统构建.md#sysbuild)，一起构建MCUboot及启用了Flash后端和MCUboot支持的示例：

```bash
# From the root of the zephyr repository
west build -b reel_board --sysbuild samples/subsys/usb/dfu -- -DSB_CONFIG_BOOTLOADER_MCUBOOT=y -DCONFIG_APP_USB_DFU_USE_FLASH_BACKEND=y
west flash
```

还需要另一个应用镜像作为固件更新，下载到SLOT-1。可以构建并签名第二个应用，例如 [Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)，用作升级镜像。不要忘记按 [MCUboot](../firmware_update/P002_设备固件升级.md#mcuboot) 说明启用所需的 [`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)。原文给出的例子为：

> 译注（原文命令边界）：上一块明确从Zephyr仓库根运行，下面的 `zephyr/samples/hello_world` 却按其父工作区布局书写，签名密钥路径也必须与实际工作区一致。因此这两块不能原样连续执行。第二个应用应使用独立构建目录，并使用与已烧录MCUboot验证配置匹配的签名密钥；已有构建目录不能直接复用成另一应用。原文还在第二个应用后写了 `west flash`，这会直接烧录该应用，可能替换正在提供DFU服务的固件。若目标是通过下一步DFU验证更新流程，第二个应用应只构建并签名，保留设备上的DFU固件，然后下载签名文件。下面完整保留原命令供核对，不将其当作连贯操作清单。

```bash
west build -b reel_board zephyr/samples/hello_world -- -DCONFIG_MCUBOOT_SIGNATURE_KEY_FILE=\"bootloader/mcuboot/root-rsa-2048.pem\" -DCONFIG_BOOTLOADER_MCUBOOT=y
west flash
```

使用下列命令将新镜像下载到设备：

```bash
dfu-util --alt 1 --download build/zephyr/zephyr.signed.bin
```

> 译注：原文的 `build/zephyr/zephyr.signed.bin` 必须指向第二个应用实际生成的签名镜像；采用独立构建目录后同步替换此相对路径。`--alt 1` 是原示例的SLOT-1选择，镜像增减会影响备用设置编号。当前Flash后端按顺序写入数据，在零长度结束块时刷新尾部缓冲。示例收到下载完成消息后，在MCUboot及Flash后端均启用时调用 `boot_request_upgrade(false)` 请求测试升级；它不会在该回调中立即复位。

复位SoC后，MCUboot会交换镜像并启动新应用，控制台输出如下：

```console
*** Booting MCUboot v2.1.0-rc1-134-gb9d69dd2a2d6 ***
*** Using Zephyr OS build v3.7.0-4345-ga5d0d8533a41 ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x4, copy_done=0x1, image_ok=0x1
I: Secondary image: magic=good, swap_type=0x2, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Image index: 0, Swap type: test
I: Starting swap using move algorithm.
I: Bootloader chainload address offset: 0xc000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build v3.7.0-4345-ga5d0d8533a41 ***
Hello World! reel_board@1/nrf52840
```

再次复位SoC后，MCUboot应回退镜像并启动USB DFU示例，输出如下：

```console
*** Booting MCUboot v2.1.0-rc1-134-gb9d69dd2a2d6 ***
*** Using Zephyr OS build v3.7.0-4345-ga5d0d8533a41 ***
I: Starting bootloader
I: Primary image: magic=good, swap_type=0x2, copy_done=0x1, image_ok=0x3
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Boot source: none
I: Image index: 0, Swap type: revert
I: Starting swap using move algorithm.
I: Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
I: Bootloader chainload address offset: 0xc000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build v3.7.0-4345-ga5d0d8533a41 ***
[00:00:00.000,335] <inf> main: USBD message: VBUS ready
[00:00:00.000,427] <inf> main: USB DFU sample is initialized
```

> 译注：两段为官方历史输出，显示测试交换（Test Swap）后未确认新镜像，再次启动执行回退（Revert）的流程；实际结果取决于MCUboot配置、槽位布局及新应用是否确认镜像，不表示任何升级都会在第二次复位时回退。本页未执行固件编译、镜像签名、上传下载或实板复位。

## 64.4\_参阅（See Also）

- [USB设备核心API](P015_USB设备核心API.md)。
- [USB DFU设备更新API](P062_USB设备固件升级API.md)。


译注核对来源：[subsys/usb/device_next/class/usbd_dfu_flash.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu_flash.c)、[samples/subsys/usb/dfu/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/dfu/src/main.c)、[samples/subsys/usb/dfu/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/dfu/Kconfig)、[samples/subsys/usb/dfu/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/dfu/prj.conf)、[samples/subsys/usb/dfu/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/dfu/app.overlay)。

本仓库的[对应源码](../../../subsys/usb/device_next/class/usbd_dfu_flash.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-dfu"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="building-with-flash-backend-enabled"></a>
<a id="see-also"></a>

[上一章](P063_USB固件升级镜像结构.md) · [返回大纲](大纲.md) · [下一章](P065_USB示例目录.md)
