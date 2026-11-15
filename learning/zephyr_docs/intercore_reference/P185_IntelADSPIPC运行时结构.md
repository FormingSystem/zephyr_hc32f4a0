---
id: learning.zephyr-docs.intercore_reference.ipchostref-185
title: IntelADSPIPC运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第185章\_IntelADSPIPC运行时结构

原文：[structintel__adsp__ipc__data](https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__ipc__data.html)。读取日期：2026-10-13，`latest`。

`intel_adsp_ipc_data`是Intel 音频数字信号处理器（Audio Digital Signal Processor，ADSP）的处理器间通信（Inter-Processor Communication，IPC）服务后端运行时数据（Run-time Data）结构，定义在`zephyr/ipc/backends/intel_adsp_host_ipc.h`。

## 185.1\_原页六个字段

| 字段 | 类型 | 原文含义 |
| --- | --- | --- |
| `sem` | `struct k_sem` | 信号量（Semaphore），用于等待远端确认已发送的消息 |
| `lock` | `struct k_spinlock` | 驱动通用锁（General Driver Lock）；类型为自旋锁（Spinlock） |
| `tx_ack_pending` | `bool` | 等待发送确认（Transmit Acknowledgment，TX ACK） |
| `ept_cfg` | `const struct ipc_ept_cfg *` | 指向端点配置（Endpoint Configuration）的指针 |
| `done_notify` | `intel_adsp_ipc_done_t` | 完成通知（Done Notification）的回调 |
| `done_arg` | `void *` | 完成通知回调的参数 |

## 185.2\_完整源码结构

```c
struct intel_adsp_ipc_data {
        struct k_sem sem;

        struct k_spinlock lock;

        bool tx_ack_pending;

        const struct ipc_ept_cfg *ept_cfg;

#ifdef CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE
        intel_adsp_ipc_handler_t handle_message;

        void *handler_arg;
#endif /* CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE */

        intel_adsp_ipc_done_t done_notify;

        void *done_arg;

#ifdef CONFIG_PM_DEVICE
        intel_adsp_ipc_resume_handler_t resume_fn;

        void *resume_fn_args;

        intel_adsp_ipc_suspend_handler_t suspend_fn;

        void *suspend_fn_args;
#endif /* CONFIG_PM_DEVICE */
};
```

## 185.3\_源码中的六个条件成员

原参考页显示上述六个无条件成员；完整源码还包含下列六个受配置控制的成员。`CONFIG_`前缀来自 Kconfig 构建配置系统（Build Configuration System）；PM 为电源管理（Power Management）。

以下用途仅根据类型和名称提供阅读说明；原参考页未列出这些成员的详细契约。

| 字段 | 类型 | 出现条件 | 阅读说明 |
| --- | --- | --- | --- |
| `handle_message` | `intel_adsp_ipc_handler_t` | `CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE` | 消息处理回调成员 |
| `handler_arg` | `void *` | `CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE` | 消息处理参数成员 |
| `resume_fn` | `intel_adsp_ipc_resume_handler_t` | `CONFIG_PM_DEVICE` | 恢复（Resume）处理回调成员 |
| `resume_fn_args` | `void *` | `CONFIG_PM_DEVICE` | 恢复处理回调参数成员 |
| `suspend_fn` | `intel_adsp_ipc_suspend_handler_t` | `CONFIG_PM_DEVICE` | 挂起（Suspend）处理回调成员 |
| `suspend_fn_args` | `void *` | `CONFIG_PM_DEVICE` | 挂起处理回调参数成员 |

完成通知回调的`true`／`false`责任区分见[IntelADSP主机IPC头文件参考](P182_IntelADSP主机IPC头文件参考.md)；端点配置类型见[IPC服务端点配置](P114_IPC服务端点配置.md)。

---

[上一章：IntelADSPIPC配置结构](P184_IntelADSPIPC配置结构.md) · [下一章：IntelADSPIPC端点私有数据](P186_IntelADSPIPC端点私有数据.md) · [返回大纲](大纲.md)
