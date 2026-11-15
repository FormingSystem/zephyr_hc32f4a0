---
id: learning.zephyr-docs.intercore_reference.ipmsample-82
title: IVSHMEM处理器间邮箱示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_ivshmem/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipm-ivshmem"></a>

# 第82章\_IVSHMEM处理器间邮箱示例

原文：[IPM over IVSHMEM](https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_ivshmem/README.html)。读取日期：2026-10-13，`latest`。

本示例通过虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）实现处理器间邮箱（Inter-Processor Mailbox，IPM）通知。VM 指虚拟机（Virtual Machine）。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 82.1\_前置条件

需要可用的QEMU模拟器，以及已经启动的`ivshmem-server`服务端程序。服务端可从Zephyr软件开发工具包（Software Development Kit，SDK）取得，某些发行版也提供预编译程序；否则可在QEMU源码树中找到。

还需要`ivshmem-client`客户端程序，本例把它用作外部应用。它也可从QEMU取得，获取条件与服务端相同。**原文措辞译注：**客户端前置条件段落误把比较对象重复写成`ivshmem-server`，这里按上下文说明客户端与服务端采用相同获取方式。

## 82.2\_准备共享内存服务端

原文给出的SDK工具位置如下，其中`/path/to/your/zephyr-sdk`为用户安装目录占位符，`<version>`为版本占位符：

```
/path/to/your/zephyr-sdk/zephyr-<version>/sysroots/x86_64-pokysdk-linux/usr/xilinx/bin/
```

同处也可能找到`ivshmem-client`，可用它检查环境是否按预期工作。

启动`ivshmem-server`时，通知向量（Notification Vector）数量和共享内存大小都在运行时（Run-time）决定。对Zephyr而言，向量数量在编译时（Compile-time）决定，共享内存大小在运行时决定。此示例的Arm64项目配置使用两个向量，原命令如下：

```sh
# n = number of vectors
$ sudo ivshmem-server -n 2
$ *** Example code, do not use in production ***
```

原注释中`n`表示向量数量；输出提醒“这是示例代码，不要用于生产环境”。

根据部署场景，为`/dev/shm/ivshmem`和`/tmp/ivshmem_socket`设置适当的所有权及访问权限。原例使用环境变量`$USER`的值指定所属组：

```sh
$ sudo chgrp $USER /dev/shm/ivshmem
$ sudo chmod 060 /dev/shm/ivshmem
$ sudo chgrp $USER /tmp/ivshmem_socket
$ sudo chmod 060 /tmp/ivshmem_socket
```

## 82.3\_分别构建两个实例

QEMU准备好后，打开两个终端，为Zephyr的west命令分别创建输出目录。第一个终端：

```sh
$ mkdir -p path/to/instance_1
```

另一个终端：

```sh
$ mkdir -p path/to/instance_2
```

本示例必须构建两次。以下是原构建命令；在第一个终端追加`-d path/to/instance_1`，在另一个终端追加`-d path/to/instance_2`：

```sh
west build -b qemu_cortex_a53 samples/drivers/ipm/ipm_ivshmem
```

运行两侧QEMU时，重复构建命令并使用运行目标（Run Target），仍需用`-d path/to/instance_x`选择对应目录，x在两个终端中分别为1或2。原命令块：

```sh
west build -b qemu_cortex_a53 samples/drivers/ipm/ipm_ivshmem
west build -t run
```

**译注：**原代码块省略了正文要求追加的`-d`选项。实际使用时，构建与`run`都应指向各自的输出目录；这里保留原代码，并明确正文中的目录选择要求。

## 82.4\_查询对端并发送通知

在一个实例的控制台执行`ivshmem`，查看其对端标识（Peer ID）：

```text
*** Booting Zephyr OS build zephyr-v3.4.0-974-g7fba7d395750 ***


uart:~$ ivshmem
IVshmem up and running:
   Shared memory: 0xafa00000 of size 4194304 bytes
   Peer id: 12
   Notification vectors: 2
uart:~$
```

原例中该实例的标识为12，共享内存大小为4194304字节，通知向量数为2。到另一个实例执行`ivshmem_ipm_send`，后跟目标标识12：

```text
*** Booting Zephyr OS build zephyr-v3.4.0-974-g7fba7d395750 ***


uart:~$ ivshmem
IVshmem up and running:
   Shared memory: 0xafa00000 of size 4194304 bytes
   Peer id: 11
   Notification vectors: 2
uart:~$ ivshmem_ipm_send 12
```

再回到标识12的实例终端，可看到通过IVSHMEM收到IPM通知：

```text
uart:~$ ivshmem
IVshmem up and running:
   Shared memory: 0xafa00000 of size 4194304 bytes
   Peer id: 12
   Notification vectors: 2
uart:~$ Received IPM notification over IVSHMEM
```

原日志版本`zephyr-v3.4.0-974-g7fba7d395750`、共享地址及标识11／12均按原样保留；目标标识应以对端实际查询结果为准。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/ipm/ipm_ivshmem)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：NXPiMX处理器间邮箱示例](P081_NXPiMX处理器间邮箱示例.md) · [下一章：NXPLPC处理器间邮箱示例](P083_NXPLPC处理器间邮箱示例.md) · [返回大纲](大纲.md)
