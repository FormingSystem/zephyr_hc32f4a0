---
id: learning.zephyr-docs.intercore_reference.ipchostref-184
title: IntelADSPIPC配置结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第184章\_IntelADSPIPC配置结构

原文：[structintel__adsp__ipc__config](https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__config.html)。读取日期：2026-10-13，`latest`。

`intel_adsp_ipc_config`是Intel 音频数字信号处理器（Audio Digital Signal Processor，ADSP）的处理器间通信（Inter-Processor Communication，IPC）服务后端配置结构（Configuration Structure），定义在`zephyr/ipc/backends/intel_adsp_host_ipc.h`。

## 184.1\_完整结构

```c
struct intel_adsp_ipc_config {
        volatile struct intel_adsp_ipc *regs;
};
```

唯一字段`regs`的完整类型是`volatile struct intel_adsp_ipc *`，指向硬件寄存器块（Hardware Register Block）。`volatile`限定符按原声明保留。

完整头文件见[IntelADSP主机IPC完整头文件](P183_IntelADSP主机IPC完整头文件.md)。

---

[上一章：IntelADSP主机IPC完整头文件](P183_IntelADSP主机IPC完整头文件.md) · [下一章：IntelADSPIPC运行时结构](P185_IntelADSPIPC运行时结构.md) · [返回大纲](大纲.md)
