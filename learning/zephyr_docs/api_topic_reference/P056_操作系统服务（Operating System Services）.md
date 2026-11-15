---
id: learning.zephyr-docs.api-topic-reference.page-56
title: 操作系统服务（Operating System Services）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_操作系统服务（Operating System Services）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__os__services.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

操作系统服务（Operating System Services）

<a id="details"></a>

操作系统服务（Operating System Services）

<a id="header-groups"></a>
<a id="groups"></a>

## 56.1\_主题（Topics）

<a id="r_sys_5Fnotify_5Fapis"></a>

相关声明：[异步通知 API（Asynchronous Notification APIs）](../memory_services/P011_异步通知接口.md)。

<a id="r_authentication"></a>

相关声明：[身份认证（Authentication）](P005_身份认证（Authentication）.md)。

身份认证（Authentication）

<a id="r_bindesc"></a>

相关声明：[二进制描述符（Binary Descriptors）](../data_utilities/P016_二进制描述符接口总览.md)。

<a id="r_subsys_5Fcpu_5Ffreq"></a>

相关声明：[CPU 频率（CPU Frequency，CPUFreq）](../power/P023_CPU调频接口.md)。

动态 CPU 频率调节（Dynamic CPU Frequency Scaling）

<a id="r_cpu_5Fload"></a>

相关声明：[CPU 负载监测器（CPU load monitor）](../observability/P049_CPU负载接口.md)。

监测 CPU 负载的模块。

<a id="r_cache_5Finterface"></a>

相关声明：[缓存接口（Cache Interface）](../cache_reference/P001_公共缓存接口.md)。

<a id="r_checksum"></a>

相关声明：[校验和（Checksum）](../checksum_reference/P001_校验和主题目录.md)。

<a id="r_cleanup_5Finterface"></a>

相关声明：[清理辅助接口（Cleanup Helper Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html)。

<a id="r_connectivity"></a>

相关声明：[连接功能（Connectivity）](P027_连接功能（Connectivity）.md)。

连接功能（Connectivity）

<a id="r_console_5Fapi"></a>

相关声明：[控制台 API（Console API）](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html)。

控制台 API（Console API）

<a id="r_crypto"></a>

相关声明：[密码处理（Crypto）](../crypto/P008_密码驱动通用接口.md)。

密码处理 API（Crypto APIs）

<a id="r_debug"></a>

相关声明：[调试（Debug）](../debug_trace_reference/P001_调试接口目录.md)。

调试服务（Debug Services）。

<a id="r_device_5Fmgmt"></a>

相关声明：[设备管理（Device Management）](P030_设备管理（Device Management）.md)。

设备管理（Device Management）

<a id="r_sys_5Fcheck_5Fapis"></a>

相关声明：[错误检查（Error checking）](../check_reference/P001_运行时检查接口.md)。

<a id="r_fota_5Fhttp"></a>

相关声明：[基于 HTTP 的固件空中升级（FOTA HTTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html)。

基于HTTP的固件空中升级（Firmware Over-the-Air）。

<a id="r_file_5Fsystem_5Fapi"></a>

相关声明：[文件系统 API（File System APIs）](../storage/P033_文件系统接口.md)。

文件系统 API（File System APIs）

<a id="r_file_5Fsystem_5Fstorage"></a>

相关声明：[文件系统存储（File System Storage）](../storage/P034_文件系统存储参考.md)。

<a id="r_flash_5Fimg_5Fapi"></a>

相关声明：[闪存映像 API（Flash image API）](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html)。

将固件映像写入闪存的抽象层。

<a id="r_heaps"></a>

相关声明：[堆管理（Heap Management）](P039_堆管理（Heap Management）.md)。

堆管理（Heap Management）

<a id="r_ipc"></a>

相关声明：[进程间通信（IPC）](../intercore_reference/P181_IPC接口总览.md)。

进程间通信（IPC）

<a id="r_instrumentation_5Fapi"></a>

相关声明：[插桩（Instrumentation）](../observability/P025_插桩接口参考.md)。

<a id="r_iterable_5Fsection_5Fapis"></a>

相关声明：[可遍历段接口（Iterable Sections APIs）。](../iterable_reference/P001_可遍历段公共接口.md)。

可遍历段接口（Iterable Sections APIs）。

<a id="r_llext_5Fapis"></a>

相关声明：[可链接、可加载扩展（Linkable loadable extensions）](../llext/P011_扩展管理API.md)。

<a id="r_logging"></a>

相关声明：[日志（Logging）。](../log_core_reference/P001_日志主题总览.md)。

日志（Logging）。

<a id="r_memory_5Fmanagement"></a>

相关声明：[内存管理（Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html)。

内存管理（Memory Management）

<a id="r_zassert"></a>

相关声明：[基于模块的断言处理（Module based assert handling）](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html)。

<a id="r_multimedia"></a>

相关声明：[多媒体（Multimedia）](P054_多媒体（Multimedia）.md)。

硬件和软件多媒体流支持。

<a id="r_mpipe"></a>

相关声明：[多媒体管线（Multimedia Pipeline）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe.html)。

通过自包含的处理元素构建媒体流。

<a id="r_net_5Fbuf"></a>

相关声明：[网络缓冲区库（Network Buffer Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html)。

网络缓冲区库（Network buffer library）

<a id="r_resource_5Fmgmt_5Fonoff_5Fapis"></a>

相关声明：[开关服务 API（On-Off Service APIs）](../memory_services/P016_开关服务接口.md)。

<a id="r_psa_5Fsecure_5Fstorage"></a>

相关声明：[PSA 安全存储 API（PSA Secure Storage API）](../storage/P022_PSA安全存储接口.md)。

<a id="r_subsys_5Fpm"></a>

相关声明：[电源管理（Power Management，PM）](../power/P031_电源管理接口分组.md)。

系统和设备电源管理。

<a id="r_precision_5Ftiming"></a>

相关声明：[精确计时（Precision Timing）。](../timing_reference/P010_精确计时接口.md)。

精确计时（Precision Timing）。

<a id="r_rtio"></a>

相关声明：[实时输入输出（Real-Time I/O，RTIO）。](../rtio_core_reference/P001_RTIO公共接口.md)。

实时输入输出（Real-Time I/O，RTIO）。

<a id="r_retention_5Fapi"></a>

相关声明：[保持数据 API（Retention API）](../storage/P014_数据保留接口参考.md)。

保持数据 API（Retention API）

<a id="r_semihost"></a>

相关声明：[半主机 API（Semihosting APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html)。

<a id="r_sensing_5Fapi"></a>

相关声明：[感知（Sensing）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html)。

高层传感器框架（High-level sensor framework）。

<a id="r_shell_5Fapi"></a>

相关声明：[命令行解释器（Shell）](../shell_core_reference/P001_Shell核心接口.md)。

<a id="r_smf"></a>

相关声明：[状态机框架 API（State Machine Framework API）](../smf/P005_状态机API参考.md)。

状态机框架 API（State Machine Framework API）

<a id="r_stats_5Fapis"></a>

相关声明：[统计信息（Statistics）。](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html)。

跟踪并报告子系统事件计数器。

<a id="r_storage_5Fapis"></a>

相关声明：[存储 API（Storage APIs）](P101_存储 API（Storage APIs）.md)。

存储 API（Storage APIs）

<a id="r_sys_5Finit"></a>

相关声明：[系统初始化（System Initialization）](../device_reference/P005_系统初始化接口.md)。

<a id="r_sys_5Fpoweroff"></a>

相关声明：[系统关机（System power off）](../power/P063_系统关机接口.md)。

<a id="r_task_5Fwdt_5Fapi"></a>

相关声明：[任务看门狗 API（Task Watchdog APIs）](../power/P009_任务看门狗接口.md)。

任务看门狗 API（Task Watchdog APIs）

<a id="r_timing_5Fapi"></a>

相关声明：[计时测量接口（Timing Measurement APIs）。](../timing_reference/P001_计时公共接口.md)。

计时测量接口（Timing Measurement APIs）。

<a id="r_subsys_5Ftracing"></a>

相关声明：[跟踪（Tracing）](../tracing_core_reference/P001_跟踪子系统总览.md)。

跟踪子系统（Tracing Subsystem）的接口。

<a id="r_xen_5Fsupport"></a>

相关声明：[Xen 支持](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html)。

Xen 虚拟机监控器（Hypervisor）支持。

<a id="r_zbus_5Fapis"></a>

相关声明：[Zbus API](../intercore_reference/P213_zbus核心接口.md)。

Zbus API

<a id="header-files"></a>
<a id="files"></a>

## 56.2\_文件（Files）

<a id="r_cmsis_5Ftypes_2Eh"></a>

```c
file cmsis_types.h
```

相关声明：[cmsis_types.h](../api_file_reference/P043_zephyr__portability__cmsis_types.h_文件参考.md)。

CMSIS-RTOSv2对象控制块（Object Control Block）结构的头文件。


## 56.3\_原页交叉引用（Cross References）

- [异步通知 API（Asynchronous Notification APIs）](../memory_services/P011_异步通知接口.md)
- [身份认证（Authentication）](P005_身份认证（Authentication）.md)
- [二进制描述符（Binary Descriptors）](../data_utilities/P016_二进制描述符接口总览.md)
- [CPU 频率（CPU Frequency，CPUFreq）](../power/P023_CPU调频接口.md)
- [CPU 负载监测器（CPU load monitor）](../observability/P049_CPU负载接口.md)
- [缓存接口（Cache Interface）](../cache_reference/P001_公共缓存接口.md)
- [校验和（Checksum）](../checksum_reference/P001_校验和主题目录.md)
- [清理辅助接口（Cleanup Helper Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html)
- [连接功能（Connectivity）](P027_连接功能（Connectivity）.md)
- [控制台 API（Console API）](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html)
- [密码处理（Crypto）](../crypto/P008_密码驱动通用接口.md)
- [调试（Debug）](../debug_trace_reference/P001_调试接口目录.md)
- [设备管理（Device Management）](P030_设备管理（Device Management）.md)
- [错误检查（Error checking）](../check_reference/P001_运行时检查接口.md)
- [基于 HTTP 的固件空中升级（FOTA HTTP）](https://docs.zephyrproject.org/latest/doxygen/html/group__fota__http.html)
- [文件系统 API（File System APIs）](../storage/P033_文件系统接口.md)
- [文件系统存储（File System Storage）](../storage/P034_文件系统存储参考.md)
- [闪存映像 API（Flash image API）](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html)
- [堆管理（Heap Management）](P039_堆管理（Heap Management）.md)
- [进程间通信（IPC）](../intercore_reference/P181_IPC接口总览.md)
- [插桩（Instrumentation）](../observability/P025_插桩接口参考.md)
- [可遍历段接口（Iterable Sections APIs）。](../iterable_reference/P001_可遍历段公共接口.md)
- [可链接、可加载扩展（Linkable loadable extensions）](../llext/P011_扩展管理API.md)
- [日志（Logging）。](../log_core_reference/P001_日志主题总览.md)
- [内存管理（Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html)
- [基于模块的断言处理（Module based assert handling）](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html)
- [多媒体（Multimedia）](P054_多媒体（Multimedia）.md)
- [多媒体管线（Multimedia Pipeline）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe.html)
- [网络缓冲区库（Network Buffer Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html)
- [开关服务 API（On-Off Service APIs）](../memory_services/P016_开关服务接口.md)
- [PSA 安全存储 API（PSA Secure Storage API）](../storage/P022_PSA安全存储接口.md)
- [电源管理（Power Management，PM）](../power/P031_电源管理接口分组.md)
- [精确计时（Precision Timing）。](../timing_reference/P010_精确计时接口.md)
- [实时输入输出（Real-Time I/O，RTIO）。](../rtio_core_reference/P001_RTIO公共接口.md)
- [保持数据 API（Retention API）](../storage/P014_数据保留接口参考.md)
- [半主机 API（Semihosting APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html)
- [感知（Sensing）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html)
- [命令行解释器（Shell）](../shell_core_reference/P001_Shell核心接口.md)
- [状态机框架 API（State Machine Framework API）](../smf/P005_状态机API参考.md)
- [统计信息（Statistics）。](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html)
- [存储 API（Storage APIs）](P101_存储 API（Storage APIs）.md)
- [系统初始化（System Initialization）](../device_reference/P005_系统初始化接口.md)
- [系统关机（System power off）](../power/P063_系统关机接口.md)
- [任务看门狗 API（Task Watchdog APIs）](../power/P009_任务看门狗接口.md)
- [计时测量接口（Timing Measurement APIs）。](../timing_reference/P001_计时公共接口.md)
- [跟踪（Tracing）](../tracing_core_reference/P001_跟踪子系统总览.md)
- [Xen 支持](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__support.html)
- [Zbus API](../intercore_reference/P213_zbus核心接口.md)
- [cmsis_types.h](../api_file_reference/P043_zephyr__portability__cmsis_types.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P055_Nuvoton 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P057_PCI Express（PCIe） API主题.md)
