---
id: learning.zephyr-docs.firmware_update.fwapi-updatehub
title: UpdateHub接口
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第31章\_UpdateHub接口

原文：[group__updatehub](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html)。读取日期：2026-10-13，`latest`。

## 31.1\_升级服务与头文件

本章是Zephyr中UpdateHub **空中固件升级（Firmware Over-The-Air，FOTA）**的 **应用程序编程接口（Application Programming Interface，API）**参考。头文件为 `zephyr/mgmt/updatehub.h`，使用流程参阅[UpdateHub升级示例](P025_UpdateHub升级示例.md)。

## 31.2\_响应状态枚举

枚举 [`updatehub_response`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga6e6eb49b1e4b558cd8be0da8b45a07b8) 向服务器与使用者表达升级状态，并统一处理错误。原声明从 `UPDATEHUB_NETWORKING_ERROR = 0` 开始，后续项目依次隐式递增。下表完整保留枚举项；中文为其名称及下文函数说明所表达的含义。

| 枚举项 | 含义 |
| --- | --- |
| [`UPDATEHUB_NETWORKING_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a) | 网络连接错误；此项数值为0。 |
| [`UPDATEHUB_INCOMPATIBLE_HARDWARE`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76) | 硬件不兼容。 |
| [`UPDATEHUB_UNCONFIRMED_IMAGE`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037) | 镜像未确认。 |
| [`UPDATEHUB_METADATA_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171) | 元数据解析或编码失败。 |
| [`UPDATEHUB_DOWNLOAD_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f) | 更新包下载失败。 |
| [`UPDATEHUB_INSTALL_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f) | 更新包安装失败。 |
| [`UPDATEHUB_FLASH_INIT_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2) | 闪存初始化失败。 |
| [`UPDATEHUB_OK`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43) | 操作成功。 |
| [`UPDATEHUB_HAS_UPDATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c) | 有可用更新。 |
| [`UPDATEHUB_NO_UPDATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730) | 无可用更新。 |

> 译注：此枚举与一般“0成功、负数失败”的整数返回约定不同，不能对返回该枚举的函数用 `rc==0` 判断成功；应与相应枚举常量比较。

## 31.3\_自动处理与镜像确认

函数 [`updatehub_autohandler()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga2a1665a1fe1b191bbc7d80c4bbaa4299) 按预定时间间隔自动执行查询与更新全过程：

```c
void updatehub_autohandler(void);
```

函数 [`updatehub_confirm()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gad1a3f6b1d91a7c9969a3411e0fd74f72) 确认当前镜像按预期运行：

```c
int updatehub_confirm(void);
```

必须在UpdateHub查询之前调用，它应是重启后尽早执行的动作之一。成功返回0，否则返回负 `errno` 错误值。

## 31.4\_查询更新

函数 [`updatehub_probe()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#ga89d1715033200c89a7587dd229944a23) 检查是否有更新需要处理：

```c
enum updatehub_response updatehub_probe(void);
```

原文列出的返回值及条件为：

| 返回值 | 条件 |
| --- | --- |
| `UPDATEHUB_HAS_UPDATE` | 有可用更新。 |
| `UPDATEHUB_NO_UPDATE` | 没有可用更新。 |
| `UPDATEHUB_NETWORKING_ERROR` | 无法连接UpdateHub服务器。 |
| `UPDATEHUB_INCOMPATIBLE_HARDWARE` | 硬件不兼容。 |
| `UPDATEHUB_METADATA_ERROR` | 无法解析或编码元数据。 |

## 31.5\_应用更新包

函数 [`updatehub_update()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gabb00cf9b63ce13554c26286c0c37fa8a) 应用更新包，必须在查询之后使用。原文说明若存在更新，它会安装新镜像并让硬件重启：

```c
enum updatehub_response updatehub_update(void);
```

| 返回值 | 条件 |
| --- | --- |
| `UPDATEHUB_OK` | 成功。 |
| `UPDATEHUB_NETWORKING_ERROR` | 无法连接服务器。 |
| `UPDATEHUB_DOWNLOAD_ERROR` | 下载更新包失败。 |
| `UPDATEHUB_INSTALL_ERROR` | 安装更新包失败。 |
| `UPDATEHUB_FLASH_INIT_ERROR` | 闪存初始化失败。 |

> 译注：本地实现的 `updatehub_update()` 安装后返回；自动处理器在收到成功状态后另调重启函数，手动示例也单独执行重启。不能仅凭原文此处的“会重启”就省略手动流程的重启步骤，应以所用版本调用路径为准。

## 31.6\_重启与上报失败

函数 [`updatehub_reboot()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gac433e995a18418771cac9fe4559ce84b) 请求系统重启：

```c
int updatehub_reboot(void);
```

原接口约定成功返回0，否则返回负 `errno`。

函数 [`updatehub_report_error()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gaa3606855ac680341e7b568421562e165) 将最近一次包更新失败报告给UpdateHub服务器：

```c
int updatehub_report_error(void);
```

它发送 **错误状态（Error State）**，协议状态标识为 `UPDATEHUB_STATE_ERROR`。成功返回0，失败返回负 `errno`。

[上一章：hawkBit事件接口](P030_hawkBit事件接口.md) · [下一章：hawkBit运行时配置结构](P032_hawkBit运行时配置结构.md) · [返回大纲](大纲.md)
