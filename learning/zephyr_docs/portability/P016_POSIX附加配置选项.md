---
id: learning.zephyr-docs.portability.page-16
title: POSIX附加配置选项
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/services/portability/posix/kconfig/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_POSIX附加配置选项

原文：[官方页面](https://docs.zephyrproject.org/latest/services/portability/posix/kconfig/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 16.1\_附加配置选项（Additional Configuration Options）

下面列出与 Zephyr POSIX API 实现相关的一部分[配置系统（Kconfig）](../kconfig/P001_配置系统概述.md#kconfig)选项；这不是完整清单。

- [`CONFIG_DYNAMIC_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_THREAD)。
- [`CONFIG_DYNAMIC_THREAD_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_THREAD_POOL_SIZE)。
- [`CONFIG_EVENTFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EVENTFD)。
- [`CONFIG_GETOPT_LONG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GETOPT_LONG)。
- [`CONFIG_MAX_PTHREAD_SPINLOCK_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAX_PTHREAD_SPINLOCK_COUNT)。
- [`CONFIG_MQUEUE_NAMELEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQUEUE_NAMELEN_MAX)。
- [`CONFIG_POSIX_MQ_OPEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MQ_OPEN_MAX)。
- [`CONFIG_MSG_SIZE_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSG_SIZE_MAX)。
- [`CONFIG_NET_SOCKETPAIR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETPAIR)。
- [`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)。
- [`CONFIG_ZVFS_POLL_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_POLL_MAX)。
- [`CONFIG_ZVFS_OPEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_OPEN_MAX)。
- [`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)。
- [`CONFIG_POSIX_OPEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_OPEN_MAX)。
- [`CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_BITS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_BITS)。
- [`CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_DEFAULT)。
- [`CONFIG_POSIX_PTHREAD_ATTR_STACKSIZE_BITS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_PTHREAD_ATTR_STACKSIZE_BITS)。
- [`CONFIG_POSIX_RTSIG_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RTSIG_MAX)。
- [`CONFIG_POSIX_SIGNAL_STRING_DESC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SIGNAL_STRING_DESC)。
- [`CONFIG_POSIX_THREAD_KEYS_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_KEYS_MAX)。
- [`CONFIG_POSIX_THREAD_THREADS_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_THREADS_MAX)。
- [`CONFIG_POSIX_UNAME_NODENAME_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_UNAME_NODENAME_LEN)。
- [`CONFIG_POSIX_UNAME_VERSION_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_UNAME_VERSION_LEN)。
- [`CONFIG_PTHREAD_CREATE_BARRIER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTHREAD_CREATE_BARRIER)。
- [`CONFIG_PTHREAD_RECYCLER_DELAY_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTHREAD_RECYCLER_DELAY_MS)。
- [`CONFIG_POSIX_SEM_NAMELEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEM_NAMELEN_MAX)。
- [`CONFIG_POSIX_SEM_NSEMS_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEM_NSEMS_MAX)。
- [`CONFIG_POSIX_SEM_VALUE_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEM_VALUE_MAX)。
- [`CONFIG_TIMER_CREATE_WAIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMER_CREATE_WAIT)。
- [`CONFIG_THREAD_STACK_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_STACK_INFO)。
- [`CONFIG_ZVFS_EVENTFD_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)。
- [`CONFIG_ZVFS_FDTABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_FDTABLE)。

译注：清单保留原页全部配置标识，不表示需要同时启用。部分项控制对象数量、名称长度、线程栈或文件描述符容量，需结合应用实际资源需求选择。[`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API) 的历史地位及子规范配置方式见[概述与配置](P011_POSIX概述与配置.md)。


<a id="additional-configuration-options"></a>
<a id="posix-kconfig-options"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：POSIX选项与选项组](P015_POSIX选项与选项组.md) · [本模块主线目录](../reading/portability.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P015_POSIX选项与选项组.md) · [返回大纲](大纲.md) · [下一章](P017_POSIX示例目录.md)

</details>

<!-- reading-navigation:end -->
