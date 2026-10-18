---
id: learning.zephyr-docs.storage.fssample-5
title: LittleFS文件系统示例
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/fs/littlefs/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="littlefs"></a>

# 第85章\_LittleFS文件系统示例

原文：[LittleFS filesystem](https://docs.zephyrproject.org/latest/samples/subsys/fs/littlefs/README.html)。读取日期：2026-10-13，`latest`。

## 85.1\_示例用途

本示例演示在 [LittleFS](https://github.com/ARMmbed/littlefs) 上使用 Zephyr 的**文件系统应用编程接口（File System API）**。示例文件分别用于记录系统启动次数，以及保存值按规定递增的二进制模式（Binary Pattern）；同时显示其他文件系统信息。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/fs/littlefs)。

## 85.2\_闪存设备与首次挂载输出

文件系统使用标签为 `storage` 的分区，参见[闪存映射（Flash Map）](https://docs.zephyrproject.org/latest/services/storage/flash_map/flash_map.html)。如果该区域没有兼容的 LittleFS 文件系统，其内容会被空文件系统替换，并出现类似诊断；日志中的 `LFS` 指 LittleFS：

```console
[00:00:00.010,192] <inf> littlefs: LittleFS version 2.0, disk version 2.0
[00:00:00.010,559] <err> littlefs: Corrupted dir pair at 0 1
[00:00:00.010,559] <wrn> littlefs: can't mount (LFS -84); formatting
```

对于新文件系统，上述错误和警告是正常的。挂载后还会看到：

```console
[00:00:00.182,434] <inf> littlefs: filesystem mounted!
[00:00:00.867,034] <err> fs: failed get file or dir stat (-2)
```

这里的错误也属正常情况，表示 Zephyr 未找到文件，本例是记录启动次数的文件。原输出版本与时间戳保持原样。

## 85.3\_块设备的主机准备

若采用**块设备（Block Device）**，如安全数字卡（Secure Digital，SD）或多媒体卡（MultiMediaCard，MMC），需先在主机上使用 `lfs` 程序准备 LittleFS 文件系统。官方链接的[主机准备说明](https://www.thevtool.com/mounting-littlefs-on-linux-machine/)是原文的外部参考。译注：此次核对该链接返回 HTTP 404，无法确认其文章内容；下方仅保留 Zephyr 页面已有的命令。

译注：以下是原文的 Linux 主机终端命令。`/dev/sda` 是原文示例设备节点，**必须先确认并替换为实际待处理卡的设备节点**；`--format` 会格式化该设备，不能把系统磁盘当作目标。`./mnt_littlefs` 是主机上的相对挂载目录。命令中的绝对设备节点属于操作参数，不是本地文档引用路径。

```shell
sudo chmod a+rw /dev/sda
lfs -d -s -f --read_size=512 --prog_size=512 --block_size=512 --cache_size=512 --lookahead_size=8192 --format /dev/sda
lfs -d -s -f --read_size=512 --prog_size=512 --block_size=512 --cache_size=512 --lookahead_size=8192 /dev/sda ./mnt_littlefs
cd ./mnt_littlefs
echo -en '\x01' > foo.txt
cd -
fusermount -u ./mnt_littlefs
```

这些步骤依次调整设备访问权限、格式化并挂载，写入包含一个字节 `0x01` 的 `foo.txt`，再卸载。命令及参数保持原样；本译文没有执行这些设备操作。

## 85.4\_闪存目标与强制重建

该示例应能在任何提供 `storage` 分区的开发板上运行；原文列出两种已测试目标，见下文。设置 `CONFIG_APP_WIPE_STORAGE` 可强制重新创建文件系统。

## 85.5\_块设备目标构建

块设备示例最初在 [Nucleo H743ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html) 上设计和测试，也可用于连接了 SD/MMC 卡的其他开发板。

在已配置 Zephyr 环境的开发终端中，从 Zephyr 源码根目录构建；`CONF_FILE=prj_blk.conf` 选择块设备配置。下面原命令还包含烧写步骤：

```shell
west build -b nucleo_h743zi samples/subsys/fs/littlefs -- -DCONF_FILE=prj_blk.conf
west flash
```

目前该示例只接受 SDMMC 和 MMC 两类块设备。最终设备树与配置中可能同时启用 `zephyr,sdmmc-disk` 和 `zephyr,mmc-disk`，挂载点名称按下列逻辑确定：

| 配置条件 | 挂载点名称 |
| --- | --- |
| 定义 [`CONFIG_DISK_DRIVER_SDMMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_SDMMC) | `SD` |
| 未定义前者，但定义 [`CONFIG_DISK_DRIVER_MMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_MMC) | `SD2` |
| 两者均未定义 | 无法确定，示例构建时报错 |

## 85.6\_nRF52840 DK与Particle Xenon

nRF52840 DK 将文件系统放在**片上系统（System on Chip，SoC）**闪存中：

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/fs/littlefs
```

Particle Xenon 将文件系统放在外部 **SPI NOR 闪存**中；SPI 是串行外设接口（Serial Peripheral Interface），NOR 为闪存类型名称。

```shell
west build -b particle_xenon samples/subsys/fs/littlefs
```

相关参考：[文件系统接口](P033_文件系统接口.md)、[闪存区域接口（Flash Area Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html)。以上保留官方目标和输出，不表示本地构建或实板验证已完成。

---

[上一章：文件系统操作示例](P084_文件系统操作示例.md) · [下一章：设置子系统示例](P086_设置子系统示例.md) · [返回大纲](大纲.md)
