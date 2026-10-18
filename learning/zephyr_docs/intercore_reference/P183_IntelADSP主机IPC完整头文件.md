---
id: learning.zephyr-docs.intercore_reference.ipchostref-183
title: IntelADSP主机IPC完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel__adsp__host__ipc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第183章\_IntelADSP主机IPC完整头文件

原文：[intel__adsp__host__ipc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/intel__adsp__host__ipc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留Intel 音频数字信号处理器（Audio Digital Signal Processor，ADSP）的处理器间通信（Inter-Processor Communication，IPC）主机后端的`zephyr/ipc/backends/intel_adsp_host_ipc.h`完整官方可见源码（Source Code）。仅去除网页行号和行尾空白，2022年、2025年的 Intel Corporation 版权及`Apache-2.0`许可证声明均原样保留。

`CONFIG_`前缀表示 Kconfig 构建配置系统（Build Configuration System）提供的配置宏。`CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE`控制旧接口（Old Interface）分支，`CONFIG_PM_DEVICE`控制设备电源管理（Device Power Management，PM）分支。回调（Callback）定义和条件成员在原代码中完整保留。

## 183.1\_完整源码

```c
/*
 * Copyright (c) 2022, 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_BACKENDS_INTEL_ADSP_HOST_IPC_H_
#define ZEPHYR_INCLUDE_IPC_BACKENDS_INTEL_ADSP_HOST_IPC_H_

#include <intel_adsp_ipc_devtree.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/pm/device.h>

#include <zephyr/ipc/ipc_service_backend.h>

#ifdef CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE

typedef bool (*intel_adsp_ipc_handler_t)(const struct device *dev, void *arg, uint32_t data,
                                         uint32_t ext_data);
#endif /* CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE */

typedef bool (*intel_adsp_ipc_done_t)(const struct device *dev, void *arg);

#ifdef CONFIG_PM_DEVICE
typedef int (*intel_adsp_ipc_resume_handler_t)(const struct device *dev, void *arg);

typedef int (*intel_adsp_ipc_suspend_handler_t)(const struct device *dev, void *arg);
#endif /* CONFIG_PM_DEVICE */

struct intel_adsp_ipc_config {
        volatile struct intel_adsp_ipc *regs;
};

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

struct intel_adsp_ipc_ept_priv_data {
        /* Message done flag. */
        bool msg_done;
        void *priv;
};

#ifdef CONFIG_PM_DEVICE

void intel_adsp_ipc_set_resume_handler(const struct device *dev, intel_adsp_ipc_resume_handler_t fn,
                                       void *arg);

void intel_adsp_ipc_set_suspend_handler(const struct device *dev,
                                        intel_adsp_ipc_suspend_handler_t fn, void *arg);

#endif /* CONFIG_PM_DEVICE */

#endif /* ZEPHYR_INCLUDE_IPC_BACKENDS_INTEL_ADSP_HOST_IPC_H_ */
```

## 183.2\_条件回调类型

`intel_adsp_ipc_done_t`始终在该头文件中定义，其完成通知契约见[IntelADSP主机IPC头文件参考](P182_IntelADSP主机IPC头文件参考.md)。下面三种类型只在相应配置下出现：


```c
typedef bool (*intel_adsp_ipc_handler_t)(const struct device *dev, void *arg, uint32_t data,
                                         uint32_t ext_data);
```

上方类型受`CONFIG_INTEL_ADSP_IPC_OLD_INTERFACE`控制。

```c
typedef int (*intel_adsp_ipc_resume_handler_t)(const struct device *dev, void *arg);
```


```c
typedef int (*intel_adsp_ipc_suspend_handler_t)(const struct device *dev, void *arg);
```

恢复和挂起处理类型受`CONFIG_PM_DEVICE`控制。原参考页未展开这些条件接口的参数说明，因此保留完整类型声明，不补写未给出的返回值约定。

同一电源管理配置下还保留`intel_adsp_ipc_set_resume_handler()`和`intel_adsp_ipc_set_suspend_handler()`两个函数声明，详见上方原始代码。

## 183.3\_可见注释与字段阅读

`intel_adsp_ipc_ept_priv_data.msg_done`前的可见注释“Message done flag.”译为“消息完成标志（Message Done Flag）”。

条件编译末尾注释标明旧接口分支和设备电源管理分支的结束；最后的头文件保护注释为`ZEPHYR_INCLUDE_IPC_BACKENDS_INTEL_ADSP_HOST_IPC_H_`。其他字段文档注释未在此网页源码中显示，已显示的参考页说明见[IntelADSPIPC配置结构](P184_IntelADSPIPC配置结构.md)、[IntelADSPIPC运行时结构](P185_IntelADSPIPC运行时结构.md)和[IntelADSPIPC端点私有数据](P186_IntelADSPIPC端点私有数据.md)。

---

[上一章：IntelADSP主机IPC头文件参考](P182_IntelADSP主机IPC头文件参考.md) · [下一章：IntelADSPIPC配置结构](P184_IntelADSPIPC配置结构.md) · [返回大纲](大纲.md)
