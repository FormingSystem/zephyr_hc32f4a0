---
id: learning.zephyr-docs.usb.page-60
title: USB大容量存储示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/mass/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_USB大容量存储示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/mass/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 60.1\_概述（Overview）

本示例演示Zephyr的USB大容量存储（USB Mass Storage，MSC）驱动。这个简单的驱动可将开发板上的RAM或Flash枚举为USB磁盘。

## 60.2\_前提条件（Requirements）

本示例需要USB设备驱动，以及96 KiB RAM或一个Flash设备。

> 译注：RAM磁盘（RAM Disk）占用的是额外存储空间，线程栈、USB缓冲区和程序本身仍需内存。当前 `ramdisk.overlay` 使用192个512字节扇区，即96 KiB；这不等于整块板只需96 KiB RAM。

## 60.3\_构建与运行（Building and Running）

示例支持多种开发板，通过Zephyr源码树中的 [samples/subsys/usb/mass/boards](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/mass/boards) 内的设备树覆盖文件（Devicetree Overlay）进行定制。使用命令行 `-D` 传入Kconfig配置，可以选择RAM磁盘、Flash磁盘和文件系统。

> 译注：以下构建命令以已具备Zephyr工作区、依赖模块、SDK及目标板工具为前提，在读者的Zephyr源码根目录执行，普通命令可用Bash。各小节是不同配置分支；改板或换配置时使用独立构建目录或按west说明重新配置，不能无条件连续粘贴。生成固件后再按所选板的官方烧录方法操作。构建失败先检查板名、覆盖文件与存储配置；USB未枚举时先检查连接的是否为设备USB口。

### 60.3.1\_不使用文件系统的RAM磁盘示例

默认配置选择不带文件系统的RAM磁盘。该示例额外使用96 KiB RAM，用于测试USB大容量存储类实现。

```bash
west build -b reel_board samples/subsys/usb/mass -- -DEXTRA_DTC_OVERLAY_FILE="ramdisk.overlay"
```

> 译注：当前Kconfig默认选择 `APP_MSC_STORAGE_NONE`，此分支不挂载文件系统；上面的 `ramdisk.overlay` 才提供RAM磁盘设备。这里的“无文件系统”不表示USB类无需磁盘访问驱动，也不承诺主机自动挂载。

### 60.3.2\_FAT文件系统（FAT File System）示例

可用RAM超过96 KiB时，可以在RAM磁盘上使用FAT文件系统。

```bash
west build -b reel_board samples/subsys/usb/mass -- -DEXTRA_DTC_OVERLAY_FILE="ramdisk.overlay" -DCONFIG_APP_MSC_STORAGE_RAM=y
```

也可以在片上系统（System on Chip，SoC）的内部Flash上使用FAT，前提是存储分区足够大。

```bash
west build -b frdm_k64f samples/subsys/usb/mass -- -DEXTRA_DTC_OVERLAY_FILE="flashdisk.overlay" -DCONFIG_APP_MSC_STORAGE_FLASH_FATFS=y -DCONFIG_DISK_DRIVER_SDMMC=n
```

SoC内部Flash的存储分区可能不足以容纳FAT文件系统。如果开发板带外部Flash，可以改用该器件。示例提供了几个配置外部Flash的板级覆盖文件。例如，原文称Adafruit Feather nRF52840 Express的覆盖文件可使用一个“16 MiBy QSPI Flash”芯片，并划出2 MiBy FAT分区。

> 译注（原文容量与板名核对）：原文段落称Express，下面的命令实际选择Sense，不能把二者视为同一板名。当前公共板级DTS的 `gd25q16` 设置 `size = <16777216>`，对应绑定明确该属性单位为bit，即16 Mibit／2 MiB，原文“16 MiBy”与此不符。示例Sense覆盖文件的分区长度为 `0x200000`，即2 MiB。四线串行外设接口（Quad Serial Peripheral Interface，QSPI）描述访问接口，并不改变容量单位。

```bash
west build -b adafruit_feather_nrf52840_sense samples/subsys/usb/mass -- -DCONFIG_APP_MSC_STORAGE_FLASH_FATFS=y
```

完成构建并将示例固件烧录到板上之后，将板连接到主机，例如运行Linux的PC。Linux主机的 `journalctl` 命令可显示设备识别信息：

```console
$ journalctl -k -n 17
usb 2-2.4: new full-speed USB device number 29 using xhci_hcd
usb 2-2.4: New USB device found, idVendor=2fe3, idProduct=0008, bcdDevice= 2.03
usb 2-2.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 2-2.4: Product: Zephyr MSC sample
usb 2-2.4: Manufacturer: ZEPHYR
usb 2-2.4: SerialNumber: 86FE679A598AC47A
usb-storage 2-2.4:1.0: USB Mass Storage device detected
scsi host3: usb-storage 2-2.4:1.0
scsi 3:0:0:0: Direct-Access     ZEPHYR   ZEPHYR USB DISK  0.01 PQ: 0 ANSI: 0 CCS
sd 3:0:0:0: Attached scsi generic sg4 type 0
sd 3:0:0:0: [sdb] 256 512-byte logical blocks: (131 kB/128 KiB)
sd 3:0:0:0: [sdb] Write Protect is off
sd 3:0:0:0: [sdb] Mode Sense: 03 00 00 00
sd 3:0:0:0: [sdb] No Caching mode page found
sd 3:0:0:0: [sdb] Assuming drive cache: write through
 sdb:
sd 3:0:0:0: [sdb] Attached SCSI removable disk
```

设备控制台输出类似如下，文件系统中的内容会不同：

```console
*** Booting Zephyr OS build zephyr-v2.3.0-1991-g4c8d1496eafb  ***
Area 4 at 0x0 on GD25Q16 for 2097152 bytes
Mount /NAND:: 0
/NAND:: bsize = 512 ; frsize = 1024 ; blocks = 2028 ; bfree = 1901
/NAND: opendir: 0
  F 0 SAMPLE.TXT
End of files
[00:00:00.077,423] <inf> main: The device is put in USB mass storage mode.
```

在多数操作系统中，该磁盘会自动挂载。

> 译注：以上是官方保留的历史日志，版本、产品字符串、磁盘大小、设备名及文件列表不应与当前配置强行对应。当前配置产品字符串为 `USBD MSC sample`。主机出现USB磁盘与文件系统成功挂载是两个阶段；排错时先确认枚举和块设备，再检查文件系统。

### 60.3.3\_SD卡（SD Card）示例

此分支需要SD卡支持，参见 [磁盘访问（Disk Access）](../storage/P008_磁盘访问.md#disk-access-api)，并准备一张已格式化为FAT的SD卡。

如果板上有SD卡控制器，可如下构建：

```bash
west build -b mimxrt1050_evk samples/subsys/usb/mass -- -DCONFIG_APP_MSC_STORAGE_SDCARD=y
```

如果板上没有SD卡控制器，但可以通过串行外设接口（Serial Peripheral Interface，SPI）连接SD卡，例如借助扩展板（Shield），可如下构建：

```bash
west build -b nrf52840dk/nrf52840 --shield waveshare_epaper_gdeh0154a07 samples/subsys/usb/mass -- -DCONFIG_APP_MSC_STORAGE_SDCARD=y
```

介质容量会影响文件系统初始化时间；初始化完成后SD卡才通过USB可用。SPI传输速度较慢，也应计入等待时间。

```console
*** Booting Zephyr OS build v2.5.0-rc3-73-gd85067f0a759  ***
Mount /SD:: 0
[00:00:00.281,585] <inf> sdhc_spi: Found a ~3751 MiB SDHC card.
[00:00:00.282,867] <inf> sdhc_spi: Manufacturer ID=27 OEM='SM' Name='00000' Revision=0x10 Serial=0x16fdd47b
[00:00:00.308,654] <inf> sdhc_spi: Found a ~3751 MiB SDHC card.
[00:00:00.309,906] <inf> sdhc_spi: Manufacturer ID=27 OEM='SM' Name='00000' Revision=0x10 Serial=0x16fdd47b
/SD:: bsize = 512 ; frsize = 32768 ; blocks = 119776 ; bfree = 119773
/SD: opendir: 0
  D 0 42
  F 1111 TEST.TXT
End of files
[00:00:18.588,043] <inf> main: The device is put in USB mass storage mode.
```

### 60.3.4\_LittleFS文件系统示例

任何定义了存储分区的开发板都可构建此示例。

```bash
west build -b reel_board samples/subsys/usb/mass -- -DEXTRA_DTC_OVERLAY_FILE="flashdisk.overlay" -DCONFIG_APP_MSC_STORAGE_FLASH_LITTLEFS=y
```

需要更多存储空间时，可以像FAT分支那样配置外部Flash。在此分支中，原文称nRF52840DK使用“64 MiB QSPI Flash”，并提供128 KiBy的 [littlefs](https://github.com/littlefs-project/littlefs) 分区，与 [LittleFS文件系统示例](../storage/P085_LittleFS文件系统示例.md) 生成的分区兼容。

> 译注（原文容量核对）：当前板级DTS的 `mx25r64` 设置 `size = <67108864>`，绑定单位为bit，即64 Mibit／8 MiB，不是64 MiB。示例覆盖文件的分区为 `0x20000` 字节，即128 KiB。芯片总容量、导出的分区容量和文件系统块数须分别核对。

```bash
west build -b nrf52840dk/nrf52840 samples/subsys/usb/mass -- -DCONFIG_APP_MSC_STORAGE_FLASH_LITTLEFS=y
```

构建并烧录后，将板的两个USB接口（调试接口和nRF USB接口）连接到支持littlefs-FUSE的操作系统主机。控制台输出类似如下，文件内容会不同：

```console
*** Booting Zephyr OS build zephyr-v2.2.0-1966-g7815942d5fc5  ***
Area 4 at 0x0 on MX25R64 for 65536 bytes
[00:00:00.005,310] <inf> main: The device is put in USB mass storage mode.

[00:00:00.009,002] <inf> littlefs: LittleFS version 2.2, disk version 2.0
[00:00:00.009,063] <inf> littlefs: FS at MX25R64:0x0 is 16 0x1000-byte blocks with 512 cye
[00:00:00.009,063] <inf> littlefs: sizes: rd 16 ; pr 16 ; ca 64 ; la 32
[00:00:00.011,718] <inf> littlefs: /lfs mounted
Mount /lfs: 0
/lfs: bsize = 16 ; frsize = 4096 ; blocks = 16 ; bfree = 13
/lfs opendir: 0
  F 8 hi
  F 128 linux
  F 5 newfile
End of files
```

在Linux或FreeBSD挂载littlefs的方法见下节。

> 译注：上述历史日志实际展示64 KiB、16个4096字节块，与前文128 KiB分区及后面的32块命令并非同一容量配置。保留日志用于对照；挂载参数必须取自当前固件实际输出。当前示例源码在准备存储时挂载并列目录，随后启用USB，并未在两者之间自动卸载本地文件系统；扩展应用时不能让主机和设备端同时修改同一文件系统。

### 60.3.5\_littlefs的使用（littlefs Usage）

很多系统能自动挂载FAT文件系统，而在Linux或FreeBSD上挂载littlefs可使用 [littlefs-FUSE](https://github.com/littlefs-project/littlefs-fuse) 工具。FUSE指用户空间文件系统（Filesystem in Userspace）。

首先从系统日志确定本地设备名，例如：

```console
Apr 25 08:10:25 tirzah kernel: [570310.921039] scsi 17:0:0:0: Direct-Access     ZEPHYR   ZEPHYR USB DISK  0.01 PQ: 0 ANSI: 0 CCS
Apr 25 08:10:25 tirzah kernel: [570310.921550] sd 17:0:0:0: Attached scsi generic sg4 type 0
Apr 25 08:10:25 tirzah kernel: [570310.922277] sd 17:0:0:0: [sdd] 256 512-byte logical blocks: (131 kB/128 KiB)
Apr 25 08:10:25 tirzah kernel: [570310.922696] sd 17:0:0:0: [sdd] Write Protect is off
```

日志表明，与该USB磁盘关联的块设备为 `/dev/sdd`：

```console
tirzah[447]$ ll /dev/sdd
brw-rw---- 1 root disk 8, 48 Apr 25 08:10 /dev/sdd
```

可使用以下命令挂载文件系统：

> 译注：本块在Linux／FreeBSD主机终端运行，前提是已安装 `lfs` 工具、确认当前USB块设备并取得访问权限。原文的 `/dev/sdd` 是示例设备节点，`/tmp/lfs` 是主机挂载点，都不是作者的仓库目录；必须按实际识别结果选设备。`chmod a+rw` 是原文向所有用户开放该设备读写的方式，不应对未核实的磁盘执行。挂载失败先对照设备和下一小节的几何参数，不据此重新格式化介质。

```bash
sudo chmod a+rw /dev/sdd   # required to allow user access
mkdir /tmp/lfs
lfs \
       --read_size=16 \
       --prog_size=16 \
       --block_size=4096 \
       --block_count=32 \
       --cache_size=64 \
       --lookahead_size=32 \
       /dev/sdd /tmp/lfs
```

输出可能如下，磁盘内容会不同：

```console
tirzah[467]$ ls -l /tmp/lfs
total 0
-rwxrwxrwx 0 root root   8 Dec 31  1969 hi
-rwxrwxrwx 0 root root 128 Dec 31  1969 linux
-rwxrwxrwx 0 root root   5 Dec 31  1969 newfile
```

`lfs` 是挂载命令；移除USB磁盘前应先卸载：

```bash
umount /tmp/lfs
```

#### (1)\_littlefs参数选择（Parameter Selection）

传给 `lfs` 的参数必须与初始化文件系统时的对应参数完全相同。可以从Zephyr挂载日志读取这些数值：

```console
[00:00:00.009,002] <inf> littlefs: LittleFS version 2.2, disk version 2.0
[00:00:00.009,063] <inf> littlefs: FS at MX25R64:0x0 is 16 0x1000-byte blocks with 512 cye
[00:00:00.009,063] <inf> littlefs: sizes: rd 16 ; pr 16 ; ca 64 ; la 32
```

- `--read_size` 对应 `rd`，为16。
- `--prog_size` 对应 `pr`，为16。
- `--block_size` 来自 `0x1000-byte blocks`，为4096（`0x1000`）。
- `--block_count` 来自 `16 0x1000-byte blocks`，为16。
- `--cache_size` 对应 `ca`，为64。
- `--lookahead_size` 对应 `la`，为32。

Zephyr和Linux两端只要有一个参数不一致，文件系统就不能正确挂载。

> 译注：原文挂载命令设置 `--block_count=32`，此处日志则要求16；必须根据当前日志选择。128 KiB／4096字节为32块，64 KiB／4096字节为16块，这两个示例不能混用。

## 60.4\_参阅（See Also）

- [USB设备核心API](P015_USB设备核心API.md)。
- [USB大容量存储类设备API](P058_USB大容量存储API.md)。
- [文件系统API](../storage/P033_文件系统接口.md)。


译注核对来源：[samples/subsys/usb/mass/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/src/main.c)、[samples/subsys/usb/mass/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/prj.conf)、[samples/subsys/usb/mass/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/Kconfig)、[samples/subsys/usb/mass/ramdisk.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/ramdisk.overlay)、[samples/subsys/usb/mass/flashdisk.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/flashdisk.overlay)、[samples/subsys/usb/mass/boards/nrf52840dk_nrf52840.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/boards/nrf52840dk_nrf52840.overlay)、[samples/subsys/usb/mass/boards/adafruit_feather_nrf52840_sense.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/mass/boards/adafruit_feather_nrf52840_sense.overlay)、[boards/adafruit/feather_nrf52840/adafruit_feather_nrf52840_common.dtsi](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/boards/adafruit/feather_nrf52840/adafruit_feather_nrf52840_common.dtsi)、[boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts)、[dts/bindings/mtd/nordic,qspi-nor.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/mtd/nordic,qspi-nor.yaml)。

本仓库的[对应源码](../../../samples/subsys/usb/mass/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-mass"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="ram-disk-example-without-any-file-system"></a>
<a id="fat-fs-example"></a>
<a id="sd-card-example"></a>
<a id="littlefs-example"></a>
<a id="littlefs-usage"></a>
<a id="littlefs-parameter-selection"></a>
<a id="see-also"></a>

[上一章](P059_USB大容量存储逻辑单元.md) · [返回大纲](大纲.md) · [下一章](P061_USB设备固件升级API说明.md)
