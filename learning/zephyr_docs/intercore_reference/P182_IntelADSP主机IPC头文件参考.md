---
id: learning.zephyr-docs.intercore_reference.ipchostref-182
title: IntelADSP主机IPC头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel__adsp__host__ipc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第182章\_IntelADSP主机IPC头文件参考

原文：[intel__adsp__host__ipc_8h](https://docs.zephyrproject.org/latest/doxygen/html/intel__adsp__host__ipc_8h.html)。读取日期：2026-10-13，`latest`。

本页对应Intel 音频数字信号处理器（Audio Digital Signal Processor，ADSP）的处理器间通信（Inter-Processor Communication，IPC）主机后端头文件`zephyr/ipc/backends/intel_adsp_host_ipc.h`。

## 182.1\_依赖头文件

```c
#include <intel_adsp_ipc_devtree.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/pm/device.h>
#include <zephyr/ipc/ipc_service_backend.h>
```

## 182.2\_数据结构

[IntelADSPIPC配置结构](P184_IntelADSPIPC配置结构.md)为后端配置，[IntelADSPIPC运行时结构](P185_IntelADSPIPC运行时结构.md)为后端运行时数据，[IntelADSPIPC端点私有数据](P186_IntelADSPIPC端点私有数据.md)为端点私有数据。

## 182.3\_消息完成回调

```c
typedef bool (*intel_adsp_ipc_done_t)(const struct device *dev, void *arg);
```

这是 Intel ADSP IPC 消息完成回调（Message Complete Callback）。通过`intel_adsp_ipc_set_done_handler()`注册后，当连接另一端发回“DONE”完成中断（Completion Interrupt），表示之前发送的消息已经处理完毕时，会在**中断上下文（Interrupt Context）**调用此回调。

**硬件注意事项：** Intel ADSP 硬件在远端设备清除中断时，同步发送 DONE 中断，不能延迟处理。此回调仍然会发生，但依赖异步命令处理通知（Asynchronous Command Processing Notification）的协议需要修改。

| 参数 | 含义 |
| --- | --- |
| `dev` | IPC 设备 |
| `arg` | 通过`intel_adsp_ipc_set_done_handler()`注册的参数 |

## 182.4\_返回值与完成责任

| 返回值 | 含义和后续责任 |
| --- | --- |
| `true` | IPC 完成操作由外部执行；接口将跳过用于通知消息完成的 IPC 寄存器写入，**外部代码必须手动完成这些操作** |
| `false` | 由此接口正常写入 IPC 寄存器，通知消息完成 |

返回值表示由谁执行完成操作，不应改写为普通的成功／失败布尔值。原文提及`intel_adsp_ipc_set_done_handler()`，但此网页和对应可见头文件没有列出该函数的声明，因此这里不补造其签名。

完整源码中的条件类型与成员见[IntelADSP主机IPC完整头文件](P183_IntelADSP主机IPC完整头文件.md)。

---

[上一章：IPC接口总览](P181_IPC接口总览.md) · [下一章：IntelADSP主机IPC完整头文件](P183_IntelADSP主机IPC完整头文件.md) · [返回大纲](大纲.md)
