---
id: learning.zephyr-docs.intercore_reference.openampsample-91
title: RenesasLinux与Zephyr通信示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/boards/renesas/openamp_linux_zephyr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="rz-openamp-linux-zephyr"></a>

# 第91章\_RenesasLinux与Zephyr通信示例

原文：[OpenAMP Linux Zephyr RPMsg](https://docs.zephyrproject.org/latest/samples/boards/renesas/openamp_linux_zephyr/README.html)。读取日期：2026-10-13，`latest`。

本应用演示Zephyr与Linux之间通过OpenAMP通信，两侧都使用OpenAMP库。Linux应用使用[meta-openamp](https://github.com/OpenAMP/meta-openamp)提供的OpenAMP库，使核间通信采用一致、标准化的方式。OpenAMP保留框架名称，RPMsg指远程处理器消息（Remote Processor Messaging）。

## 91.1\_构建Zephyr应用

RZ/G3S-SMARC目标：

```sh
west build -b rzg3s_smarc/r9a08g045s33gbg/cm33 samples/boards/renesas/openamp_linux_zephyr
```

RZ/V2L-SMARC目标：

```sh
west build -b rzv2l_smarc/r9a07g054l23gbg/cm33 samples/boards/renesas/openamp_linux_zephyr
```

## 91.2\_配置RZ/G3S的Linux环境

原代码中的`LPRINTF`是日志打印接口，两个失败消息分别表示初始化RPMsg虚拟设备失败、释放可用性标志失败；RPMSG是日志中RPMsg的全大写写法。



原文支持的版本为Linux RZ/G Multi-OS Package v3.0.0。Multi-OS Package即多操作系统软件包；OS表示操作系统（Operating System）。

1. 按[参考资料1：RZ/G3S多操作系统软件包快速入门指南](https://www.renesas.com/en/document/qsg/quick-start-guide-rzg3s-multi-os-package)的“3.2 Integration of Multi-OS Package related stuff”（集成多操作系统软件包相关内容）完成准备，**暂不启动构建**。
2. 按[参考资料2：RZ/G3S开发板编程与调试](https://docs.zephyrproject.org/latest/boards/renesas/rzg3s_smarc/doc/index.html#programming-and-debugging)添加构建参数`PLAT_M33_BOOT_SUPPORT=1`。
3. 在`meta-rz-features/meta-rz-multi-os/meta-rzg3s/recipes-example/rpmsg-sample/files/platform_info.c`中插入原页高亮的代码，完整上下文如下。

```c
if (ret) {
LPRINTF("failed rpmsg_init_vdev");
goto err;
}
/* RPMsg virtio enables callback for avail flags */
ret = virtqueue_enable_cb(rpmsg_vdev->rvq);
if (ret) {
   LPRINTF("Failed release availability flags");
   goto err;
}
#ifndef __linux__ /* uC3 */
start_ipi_task(rproc);
#endif
return rpmsg_virtio_get_rpmsg_device(rpmsg_vdev);
```

**高亮范围说明：**原页要求新增的是从`/* RPMsg virtio enables callback for avail flags */`注释开始，到`virtqueue_enable_cb(rpmsg_vdev->rvq)`之后错误分支的右花括号结束，共六行。也就是启用可用标志（Avail Flags）的回调（Callback），并在返回非零时打印失败消息、跳转到`err`；上下文其余行不是这一高亮新增范围。

完成修改后启动构建。部署引导程序（Bootloader）、Linux内核镜像、设备树（Devicetree）和根文件系统（Root Filesystem，rootfs）时，参见[参考资料3：RZ/G3S Linux启动指南](https://www.renesas.com/en/document/gde/smarc-evk-rzg3s-linux-start-guide-rev106)。

## 91.3\_配置RZ/V2L的Linux环境

原文支持的版本为Linux RZ/V Multi-OS Package v3.1.1。

1. 执行[参考资料4：RZ/V2L开发板烧录说明](https://docs.zephyrproject.org/latest/boards/renesas/rzv2l_smarc/doc/index.html#flashing)的“Flashing”（烧录）章节步骤1和2。
2. 在`meta-rz-features/meta-rz-multi-os/meta-rzv2l/recipes-example/rpmsg-sample/files/platform_info.c`中插入原页高亮代码：

```c
if (ret) {
LPRINTF("failed rpmsg_init_vdev");
goto err;
}
/* RPMsg virtio enables callback for avail flags */
ret = virtqueue_enable_cb(rpmsg_vdev->rvq);
if (ret) {
   LPRINTF("Failed release availability flags");
   goto err;
}
#ifndef __linux__ /* uC3 */
start_ipi_task(rproc);
#endif
return rpmsg_virtio_get_rpmsg_device(rpmsg_vdev);
```

该平台高亮的新增范围同样为上述注释、`virtqueue_enable_cb`调用和错误分支共六行。原注释意思是“RPMsg virtio为可用标志启用回调”；失败输出字符串与`#ifndef __linux__ /* uC3 */`等原上下文均保留。

随后启动构建。部署引导程序文件、Linux内核镜像、设备树和根文件系统时，执行参考资料4的“Flashing”步骤4至8。

## 91.4\_配置Zephyr与串口

按所用开发板“Flashing”章节说明，把示例烧录到板上。使用minicom、PuTTY等串口终端（Serial Terminal），配置速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。

## 91.5\_Linux端运行与原始输出

打开Linux命令行（Shell），可通过minicom或安全外壳（Secure Shell，SSH）连接，并以`root`登录：

```text
smarc-<device> login: root
```

运行客户端命令：

```sh
root@smarc-<device>:~# rpmsg_sample_client 0 0
```

原预期输出如下。日志中IRQ为中断请求（Interrupt Request），IPI为处理器间中断（Inter-Processor Interrupt）；`CM33`是原日志中的Cortex-M33标签。程序依次初始化设备与共享缓冲区，发送载荷（Payload）、接收回显（Echo），最后给出测试错误数。

```text
root@smarc-<device>:~# rpmsg_sample_client 0 0
[211] proc_id:0 rsc_id:0 mbx_id:0
metal: info:      metal_uio_dev_open: No IRQ for device 10400000.mbox-uio.
metal: info:      metal_uio_dev_open: No IRQ for device 11010000.cpg-uio.
[211] Successfully probed IPI device
metal: info:      metal_uio_dev_open: No IRQ for device 42f00000.rsctbl.
[211] Successfully open uio device: 42f00000.rsctbl.
[211] Successfully added memory device 42f00000.rsctbl.
metal: info:      metal_uio_dev_open: No IRQ for device 43000000.vring-ctl0.
[211] Successfully open uio device: 43000000.vring-ctl0.
[211] Successfully added memory device 43000000.vring-ctl0.
metal: info:      metal_uio_dev_open: No IRQ for device 43200000.vring-shm0.
[211] Successfully open uio device: 43200000.vring-shm0.
[211] Successfully added memory device 43200000.vring-shm0.
metal: info:      metal_uio_dev_open: No IRQ for device 43100000.vring-ctl1.
[211] Successfully open uio device: 43100000.vring-ctl1.
[211] Successfully added memory device 43100000.vring-ctl1.
metal: info:      metal_uio_dev_open: No IRQ for device 43500000.vring-shm1.
[211] Successfully open uio device: 43500000.vring-shm1.
[211] Successfully added memory device 43500000.vring-shm1.
metal: info:      metal_uio_dev_open: No IRQ for device 42f01000.mhu-shm.
[211] Successfully open uio device: 42f01000.mhu-shm.
[211] Successfully added memory device 42f01000.mhu-shm.
[211] Initialize remoteproc successfully.
[211] proc_id:1 rsc_id:1 mbx_id:0
[211] Initialize remoteproc successfully.
[211] proc_id:0 rsc_id:0 mbx_id:1
[211] Initialize remoteproc successfully.
[211] proc_id:1 rsc_id:1 mbx_id:1
[211] Initialize remoteproc successfully.
[217] thread start
[CM33] creating remoteproc virtio
[CM33] initializing rpmsg shared buffer pool
[CM33] initializing rpmsg vdev
[CM33]  1 - Send data to remote core, retrieve the echo and validate its integrity ..
[CM33] Remote proc init.
[CM33] RPMSG endpoint has created. rp_ept:0xffff9c86f870
[CM33] register sig:2 succeeded.
[CM33] register sig:15 succeeded.
[CM33] RPMSG service has created.
[CM33] sending payload number 0 of size 17
[CM33]  received payload number 0 of size 17
[CM33] sending payload number 1 of size 18
[CM33]  received payload number 1 of size 18

[snip]

[CM33] sending payload number 471 of size 488
[CM33]  received payload number 471 of size 488
[CM33] ************************************
[CM33]  Test Results: Error count = 0
[CM33] ************************************
[CM33] Quitting application .. Echo test end
[CM33] Stopping application...
[211] 42f00000.rsctbl closed
[211] 43000000.vring-ctl0 closed
[211] 43200000.vring-shm0 closed
[211] 43100000.vring-ctl1 closed
[211] 43500000.vring-shm1 closed
[211] 42f01000.mhu-shm closed
```

输出中的`[snip]`是原文已有省略标记；最后显示载荷471、大小488和错误计数0，随后关闭设备。全部地址、指针和计数均为原文样例值，并非本次实测。

## 91.6\_Zephyr端原始输出

Zephyr控制台输出应用与线程启动、远端Linux应答演示启动、收到`rpmsg-service-0`服务消息，以及应答结束：

```text
*** Booting Zephyr OS build zephyr-v#.#.#-####-g########## ***
I: Starting application..!
I: Starting application threads!
I: OpenAMP[remote]  linux responder demo started
I: new_service_cb: message received from service rpmsg-service-0
I: OpenAMP[remote] Linux sample client responder started
I: OpenAMP demo ended
I: OpenAMP Linux sample client responder ended
```

## 91.7\_参考资料

**访问译注（2026-10-13）：**参考资料1和3的瑞萨文档地址在本次自动访问检查中均返回403（Forbidden，拒绝访问），因此未核验其文档内容。原链接保留；这一访问限制不表示已确认文档失效。

本页的四项原参考资料已分别链接在对应步骤中：RZ/G3S快速入门指南、RZ/G3S开发板编程调试、RZ/G3S Linux启动指南及RZ/V2L开发板烧录章节。软件包版本要求按读取到的官方原文保留，没有替换为推测的新版本。

另见[邮箱接口（Mailbox，MBOX）](P014_邮箱驱动公共接口.md)。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/boards/renesas/openamp_linux_zephyr)。

---

[上一章：RPMsg服务示例](P090_RPMsg服务示例.md) · [下一章：IPC服务使用指南](P092_IPC服务使用指南.md) · [返回大纲](大纲.md)
