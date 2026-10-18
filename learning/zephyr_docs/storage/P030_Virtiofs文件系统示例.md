---
id: learning.zephyr-docs.storage.virtiofs-0
title: Virtiofs文件系统示例
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/fs/virtiofs/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="virtiofs"></a>

# 第30章\_Virtiofs文件系统示例

原文：[virtiofs filesystem](https://docs.zephyrproject.org/latest/samples/subsys/fs/virtiofs/README.html)。读取日期：2026-10-13，`latest`。

## 30.1\_概述与前提

此示例通过 [virtiofs 文件系统](https://virtio-fs.gitlab.io/)执行文件与目录的读取、创建和列出操作，展示 Zephyr [文件系统应用程序编程接口（File System API）](https://docs.zephyrproject.org/latest/services/storage/file_system/index.html#file-system-api)的使用。virtiofs 挂载到 Zephyr 中的文件系统实际对应**主机（Host）**上的一个目录。

运行此示例需要 [virtiofsd](https://gitlab.com/virtio-fs/virtiofsd)，它是提供共享目录访问的主机侧服务程序。[示例源码目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/fs/virtiofs)包含程序和准备脚本。

## 30.2\_构建

使用工作区管理工具 west，为 QEMU 模拟目标 `qemu_x86_64` 构建：

```shell
west build -b qemu_x86_64 samples/subsys/fs/virtiofs
```

## 30.3\_手动运行

启动 QEMU 前，必须先运行 virtiofsd。静态的 `vhost-user-fs-pci` 设备通过配置项 `CONFIG_QEMU_EXTRA_FLAGS` 配置到镜像中；与之配套、用于选择**套接字（Socket）**路径的 `-chardev socket` 参数在运行时提供，因此路径可以自行选择。

先让 virtiofsd 使用选定的套接字：

```shell
virtiofsd --socket-path=/tmp/vhostqemu --shared-dir shared_dir_path
```

其中 `shared_dir_path` 是要挂载到 Zephyr 一侧的主机目录。然后通过环境变量 `QEMU_EXTRA_FLAGS`，让 QEMU 连接同一个套接字并启动：

```shell
export QEMU_EXTRA_FLAGS="-chardev socket,id=char0,path=/tmp/vhostqemu"
west build -t run
```

译注：以上命令保留官方 Unix 主机示例。代码中的套接字路径与文件系统挂载路径是示例运行参数，不是本译文目录的文件链接。

## 30.4\_通过Twister运行

也可以使用 **Twister 测试运行器（Twister）**的 virtiofs **测试执行适配器（Harness）**自动运行示例。它会为每次运行建立专用套接字并启动 virtiofsd；若未安装 virtiofsd，则跳过测试。

```shell
scripts/twister -p qemu_x86_64 -T samples/subsys/fs/virtiofs
```

## 30.5\_示例行为与输出

示例列出已挂载文件系统中的文件和目录，并打印挂载目录下名为 `file` 的文件内容。示例还会创建一些文件和目录。可以使用 `prepare_sample_directory.sh` 准备示例目录。

官方示例输出如下，其中 `Zephyr OS` 表示 Zephyr **操作系统（Operating System，OS）**：

```text
*** Booting Zephyr OS build v4.1.0-rc1-28-gc6816316fc50 ***
/virtiofs directory tree:
- dir2 (type=dir)
  - b (type=file, size=3)
  - a (type=file, size=2)
  - c (type=file, size=4)
- dir (type=dir)
  - some_file (type=file, size=0)
  - nested_dir (type=dir)
     - some_other_file (type=file, size=0)
- file (type=file, size=27)

/virtiofs/file content:
this is a file on the host
```

运行结束后，可以在主机共享目录中检查新创建的文件：

```text
shared_dir_path$ cat file_created_by_zephyr
hello world
shared_dir_path$ cat second_file_created_by_zephyr
lorem ipsum
```

译注：以上为官方示例输出，包含原文记录的 Zephyr 构建版本；不是本翻译任务实际运行所得。

## 30.6\_相关接口

- [文件系统接口参考（File System APIs）](P033_文件系统接口.md)。
- [VirtIO基础与驱动说明](../hardware/P570_VirtIO虚拟设备.md)。

---

[上一章：VirtIO块设备驱动](P029_VirtIO块设备驱动.md) · [下一章：Virtiofs头文件](P031_Virtiofs头文件.md) · [返回大纲](大纲.md)
