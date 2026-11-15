---
id: learning.zephyr-docs.driver_samples.page-67
title: IVSHMEM门铃示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/virtualization/ivshmem/doorbell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ivshmem-doorbell"></a>

# 第67章\_IVSHMEM门铃示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/virtualization/ivshmem/doorbell/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 67.1 概述（Overview）

本示例展示不同操作系统中的两个进程如何使用虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）通信。这是OpenAMP所提供功能的一个子集。

<a id="prerequisites"></a>

## 67.2 前提条件（Prerequisites）

需要有可用的QEMU。

需要有可用且正在运行的`ivshmem-server`。Zephyr SDK提供该服务端，某些发行版也提供预构建版本；否则可以从QEMU源码树获得。

还需要可用的`ivshmem-client`，本示例将其用作外部应用。它与`ivshmem-server`的获取条件相同，也可以通过QEMU获得。

> 译注——原文笔误：介绍客户端的最后一句重复写了`ivshmem-server`；结合该段主语，这里按客户端也可通过QEMU获得的含义翻译。门铃（Doorbell）指用中断通知对端处理共享内存中的内容，数据本身仍位于共享内存。

<a id="building-and-running"></a>

## 67.3 构建与运行（Building and Running）

以下是`ivshmem-doorbell`的三个原始构建与运行分支。构建从Zephyr源码根目录执行；运行前先满足下一节的服务端准备条件。

<a id="qemu-cortex-a53"></a>

### 67.3.1 Cortex-A53 QEMU（qemu\_cortex\_a53）

```sh
west build -b qemu_cortex_a53 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

<a id="qemu-kvm-arm64"></a>

### 67.3.2 Arm64 KVM QEMU（qemu\_kvm\_arm64）

```sh
west build -b qemu_kvm_arm64 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

<a id="qemu-x86-64"></a>

### 67.3.3 x86-64 QEMU（qemu\_x86\_64）

```sh
west build -b qemu_x86_64 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

<a id="how-to"></a>

## 67.4 操作方法（How to）

> 注意：对IVSHMEM共享内存的不当操作可能使QEMU崩溃，并使Zephyr停止运行。更多信息见[安全性](#security)一节。

> 注意：由于`qemu_x86_64`设备树源码（DTS）中可用随机存取存储器（RAM）有限，该平台不能使用IVSHMEM默认的4 MB共享内存大小。

复现本示例的步骤如下。

1. 运行`ivshmem-server`。对服务端而言，中断向量（Vector）数量和共享内存大小均在运行时，即启动服务端时决定。对Zephyr而言，IVSHMEM向量数量在编译时确定，共享内存大小在运行时确定。

   Arm64：本示例的项目配置使用2个向量，即`vectors == 2`。例如：

```sh
# n = number of vectors
$ sudo ivshmem-server -n 2
$ *** Example code, do not use in production ***
```

   x86-64：默认共享内存大于该平台的可用内存。对随附的示例配置，使用：

```sh
# n = number of vectors, l = shared memory size
$ sudo ivshmem-server -n 2 -l 4096
$ *** Example code, do not use in production ***
```

   可选：若`vectors != 2`，需要修改IVSHMEM驱动配置[`CONFIG_IVSHMEM_MSI_X_VECTORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_MSI_X_VECTORS)。

2. 根据部署场景，正确设置`/dev/shm/ivshmem`和`/tmp/ivshmem_socket`的所有权。例如：

```sh
# assumption: "ivshmem" group should be the only allowed to access ivshmem
$ sudo chgrp ivshmem /dev/shm/ivshmem
$ sudo chmod 060 /dev/shm/ivshmem
$ sudo chgrp ivshmem /tmp/ivshmem_socket
$ sudo chmod 060 /tmp/ivshmem_socket
$
```

3. 运行Zephyr：

```text
$ west build -t run
-- west build: running target run
[0/1] To exit from QEMU enter: 'CTRL+a, x'[QEMU] CPU: cortex-a53
*** Booting Zephyr OS build zephyr-v3.3.0-1649-g612f49da5dee ***
Use write_shared_memory.sh and ivshmem-client to send a message
```

4. 向共享内存写入消息。共享内存大小必须与`ivshmem-server`指定的大小保持一致，这正是`write_shared_memory`脚本的用途；不遵守这一大小约束可能导致QEMU崩溃。例如：

   Arm64：写入简单的“hello world”消息，脚本默认使用`ivshmem-server`的默认大小：

```sh
# ./write_shared_memory.sh -m "your message"
$ ./write_shared_memory.sh -m "hello world"
$
```

   x86-64：写入简单的“hello world”消息：

```sh
# ./write_shared_memory.sh -m "your message" -s <size of shared memory>
# assumption: the user created ivshmem-server with size 4096
$ ./write_shared_memory.sh -m "hello world" -s 4096
$
```

5. 向来宾系统（Guest）发送中断。例如使用`ivshmem-client`：

```text
# find out client id. In this execution, it is 0 (peer_id)
$ ivshmem-client
dump: dump peers (including us)
int <peer> <vector>: notify one vector on a peer
int <peer> all: notify all vectors of a peer
int all: notify all vectors of all peers (excepting us)
listen on server socket 3
cmd> dump
our_id = 1
vector 0 is enabled (fd=7)
vector 1 is enabled (fd=8)
peer_id = 0
vector 0 is enabled (fd=5)
vector 1 is enabled (fd=6)
cmd> int 0 0
```

6. 每当收到任意IVSHMEM向量上的中断，示例都会打印共享内存中的文字。以下是Arm64的输出示例：

```text
$ west build -t run
-- west build: running target run
[0/1] To exit from QEMU enter: 'CTRL+a, x'[QEMU] CPU: cortex-a53
*** Booting Zephyr OS build zephyr-v3.3.0-1649-g612f49da5dee ***
Use write_shared_memory.sh and ivshmem-client to send a message
received IRQ and full message: hello world
```

> 译注——路径、身份和大小：上面的`$`、`cmd>`及紧随命令的日志是原记录中的提示符和输出，不是每行都应输入的命令。`/dev/shm/ivshmem`与`/tmp/ivshmem_socket`属于运行服务端的Linux主机，不依赖文档仓库位置；`ivshmem`组是原例假定已经存在的授权组。客户端ID应通过当前会话的`dump`结果确定，不能永远使用示例中的0。主机写入脚本来自[示例目录](../../../samples/drivers/virtualization/ivshmem/doorbell/write_shared_memory.sh)，执行`./write_shared_memory.sh`前应进入该脚本所在目录。当前官方[脚本](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/virtualization/ivshmem/doorbell/write_shared_memory.sh)默认大小为4194304字节（4 MiB），通过截断消息或补零写入指定大小；`-s 4096`必须与该次服务端的`-l 4096`对应，不能让不同参与者采用不同大小。

<a id="known-issues"></a>

## 67.5 已知问题（Known Issues）

尽管通信由主机应用（Host Application）发起，仍应先启动来宾应用，再启动主机应用。这是因为来宾实际注册中断请求（Interrupt Request，IRQ）需要时间：需要启用PCI、映射基址寄存器（Base Address Registers，BAR）、使能IRQ并设置回调。若先初始化主机应用，来宾可能丢失第一次IRQ，使协议无法工作。

> 译注——顺序：这里的“主机应用”指发起通信的客户端，不能据此把服务端也延后到来宾之后。前述操作顺序仍是先准备服务端和访问权限，再启动Zephyr来宾，待中断注册就绪后写消息并由客户端发通知。当前官方[ivshmem.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/virtualization/ivshmem/doorbell/src/ivshmem.c)为各向量注册轮询信号，等待通知后复制共享内存并打印；它也区分消息是否截断。仓库内的[对应实现](../../../samples/drivers/virtualization/ivshmem/doorbell/src/ivshmem.c)可用于相对路径跟踪，版本差异需另行核对。

<a id="security"></a>
<a id="ivshmem-doorbell-sample-security"></a>

## 67.6 安全性（Security）

本示例假定共享内存区域大小保持不变。因此，在PCI配置期间确定内存后，不应再改变其大小。编写应用并使用[`mmap()`](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#ac2e7d057b16f0c959ffb39d8719eb1ed)时较容易做到这一点；但Shell工具（例如`echo`）会把共享内存视为文件，并可能把其大小覆盖成输入数据的长度。

保持一致性的一种方法包括两点：

1. 仅允许可信用户访问共享内存。具有不当访问权限的恶意用户可以很容易地把内存大小截断为零，例如使用`truncate`。应用仍试图读取最初较大的范围时，QEMU就可能崩溃。
2. 确保每次写入都遵守共享内存区域的大小约束。

<a id="see-also"></a>

## 67.7 另请参阅（See also）

- [虚拟机间共享内存（Inter-VM Shared Memory）](../intercore_reference/P214_IVSHMEM共享内存接口.md)。


对应官方文档源码：[samples/drivers/virtualization/ivshmem/doorbell/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/virtualization/ivshmem/doorbell/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/virtualization/ivshmem/doorbell/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P066_虚拟化示例目录.md) · [返回大纲](大纲.md)
