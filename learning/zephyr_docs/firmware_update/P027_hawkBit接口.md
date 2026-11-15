---
id: learning.zephyr-docs.firmware_update.fwapi-hawkbit
title: hawkBit接口
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_hawkBit接口

原文：[group__hawkbit](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html)。读取日期：2026-10-13，`latest`。

## 27.1\_接口范围与头文件

本章是Zephyr中hawkBit **空中固件升级（Firmware Over-The-Air，FOTA）**的 **应用程序编程接口（Application Programming Interface，API）**参考，包含状态枚举、设备身份与自定义数据回调，以及初始化、查询和重启入口。

包含头文件 [`zephyr/mgmt/hawkbit/hawkbit.h`](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)。原页面同时链接[自动处理接口](P028_hawkBit自动处理接口.md)、[配置接口](P029_hawkBit配置接口.md)与[事件接口](P030_hawkBit事件接口.md)。完整使用流程见[hawkBit升级示例](P024_hawkBit升级示例.md)。下列C声明来自原页函数与类型签名，按声明形式整理。

## 27.2\_自定义数据回调

函数指针类型 [`hawkbit_config_device_data_cb_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga2774769ec44f2793895b5d783b4dceda) 定义 **自定义数据回调（Custom Data Callback）**，向服务器提供设备特有信息：

```c
typedef int (*hawkbit_config_device_data_cb_handler_t)(
    const char *device_id, uint8_t *buffer, const size_t buffer_size);
```

参数 `device_id` 是设备标识，`buffer` 是写入 **JavaScript对象表示法（JavaScript Object Notation，JSON）**数据的缓冲区，`buffer_size` 是其大小。原参考未在此条目说明回调的整数返回约定。**译注：**本地调用点将任何非零返回值视为JSON编码失败，回调应以0表示成功；不能把已写入字节数作为成功返回值。

函数 [`hawkbit_set_custom_data_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gad8e83255a969eb61244b1edfd0b95e5d) 设置该回调：

```c
int hawkbit_set_custom_data_cb(hawkbit_config_device_data_cb_handler_t cb);
```

`cb` 是回调函数；成功返回0，传入空指针 `NULL` 时返回无效参数错误 `-EINVAL`。

## 27.3\_设备身份回调

函数指针类型 [`hawkbit_get_device_identity_cb_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga154220c632a7594c0630cdcd79385055) 定义 **设备身份（Device Identity）**获取回调：

```c
typedef bool (*hawkbit_get_device_identity_cb_handler_t)(char *id, int id_max_len);
```

`id` 指向保存设备身份的缓冲区，`id_max_len` 为其最大长度。原条目列出了布尔返回类型，但未另写返回值说明。

函数 [`hawkbit_set_device_identity_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga4ce085b8f2bb46af2c2e9f3f2879d633) 设置自定义身份回调：

```c
int hawkbit_set_device_identity_cb(hawkbit_get_device_identity_cb_handler_t cb);
```

参数 `cb` 为回调函数；成功返回0，回调为空返回 `-EINVAL`。

## 27.4\_hawkBit响应状态

枚举 [`hawkbit_response`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b) 用于向服务器和使用者表达处理状态，并统一可能发生的错误。下表完整保留原枚举项与含义；它们是hawkBit结果类别，不是通用错误编号 `errno` 的负错误码。

| 枚举项 | 含义 |
| --- | --- |
| [`HAWKBIT_NO_RESPONSE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9) | 指定时间内未收到匹配事件。 |
| [`HAWKBIT_UPDATE_INSTALLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) | 更新已安装，需要重启才能应用。 |
| [`HAWKBIT_NO_UPDATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) | 没有可用更新。 |
| [`HAWKBIT_NETWORKING_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) | 无法连接hawkBit服务器。 |
| [`HAWKBIT_UNCONFIRMED_IMAGE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) | 镜像尚未确认。 |
| [`HAWKBIT_PERMISSION_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) | 无法取得访问服务器的许可。 |
| [`HAWKBIT_METADATA_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) | 无法解析或编码元数据。 |
| [`HAWKBIT_DOWNLOAD_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) | 下载更新包时失败。 |
| [`HAWKBIT_ALLOC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01) | 内存分配失败。 |
| [`HAWKBIT_NOT_INITIALIZED`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708) | hawkBit尚未初始化。 |
| [`HAWKBIT_PROBE_IN_PROGRESS`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6) | 查询正在进行。 |

## 27.5\_初始化与更新查询

函数 [`hawkbit_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga0ef6151f205088405de242e012984ca6) 初始化闪存分区：

```c
int hawkbit_init(void);
```

成功返回0，失败返回负 `errno` 错误值。

函数 [`hawkbit_probe()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga525173f0c3d0ca4e26124a34d098d0b9) 执行 **更新查询（Probe）**，检查是否有更新需要处理：

```c
enum hawkbit_response hawkbit_probe(void);
```

返回值来自上面的 [`hawkbit_response`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b) 枚举。

## 27.6\_重启与重置动作编号

函数 [`hawkbit_reboot()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga03631b12a4107d660bac14bfd33bfebd) 请求系统重启，无返回值：

```c
void hawkbit_reboot(void);
```

函数 [`hawkbit_reset_action_id()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga26f0066c87c57b500170ac377b560bb4) 重置存储在设置中的hawkBit **动作编号（Action ID）**。更换hawkBit服务器后应执行此操作：

```c
int hawkbit_reset_action_id(void);
```

成功返回0；查询正在执行时返回稍后重试错误常量 `-EAGAIN`；无法重置动作编号时返回输入输出错误常量 `-EIO`。这些函数的调用具有设备状态效果，本章仅记录接口契约。

[上一章：OSDP设备协议示例](P026_OSDP设备协议示例.md) · [下一章：hawkBit自动处理接口](P028_hawkBit自动处理接口.md) · [返回大纲](大纲.md)
