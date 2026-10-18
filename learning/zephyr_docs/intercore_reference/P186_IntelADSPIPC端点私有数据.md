---
id: learning.zephyr-docs.intercore_reference.ipchostref-186
title: IntelADSPIPC端点私有数据
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__ept__priv__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第186章\_IntelADSPIPC端点私有数据

原文：[structintel__adsp__ipc__ept__priv__data](https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__ept__priv__data.html)。读取日期：2026-10-13，`latest`。

`intel_adsp_ipc_ept_priv_data`是Intel 音频数字信号处理器（Audio Digital Signal Processor，ADSP）的处理器间通信（Inter-Processor Communication，IPC）后端的端点私有数据（Endpoint Private Data）结构，定义在`zephyr/ipc/backends/intel_adsp_host_ipc.h`。

## 186.1\_完整结构

```c
struct intel_adsp_ipc_ept_priv_data {
        /* Message done flag. */
        bool msg_done;
        void *priv;
};
```

## 186.2\_字段说明

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `msg_done` | `bool` | 消息完成标志（Message Done Flag）；此说明来自源码可见注释 |
| `priv` | `void *` | 指向额外私有数据（Additional Private Data）的指针 |

原字段参考仅对`priv`给出文字描述；`msg_done`的注释在[IntelADSP主机IPC完整头文件](P183_IntelADSP主机IPC完整头文件.md)中保留并译出。

---

[上一章：IntelADSPIPC运行时结构](P185_IntelADSPIPC运行时结构.md) · [下一章：RPMsg串口设备树绑定](P187_RPMsg串口设备树绑定.md) · [返回大纲](大纲.md)
