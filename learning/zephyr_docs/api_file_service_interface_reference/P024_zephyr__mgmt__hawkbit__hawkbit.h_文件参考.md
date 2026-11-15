---
id: learning.zephyr-docs.api-file-service-interface-reference.page-24
title: zephyr__mgmt__hawkbit__hawkbit.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_mgmt\_\_hawkbit\_\_hawkbit.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

hawkBit的主头文件（Main Header File）。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

hawkBit的主头文件（Main Header File）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.1\_类型定义（Typedefs）

<a id="r_ga2774769ec44f2793895b5d783b4dceda"></a>

```c
typedef int(* hawkbit_config_device_data_cb_handler_t) (const char *device_id, uint8_t *buffer, const size_t buffer_size)
```

相关声明：[hawkbit_config_device_data_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga2774769ec44f2793895b5d783b4dceda)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 hawkBit 服务器提供自定义数据（Custom Data）的回调。

<a id="r_ga154220c632a7594c0630cdcd79385055"></a>

```c
typedef bool(* hawkbit_get_device_identity_cb_handler_t) (char *id, int id_max_len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[hawkbit_get_device_identity_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga154220c632a7594c0630cdcd79385055)。

获取设备身份（Device Identity）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.2\_枚举（Enumerations）

<a id="r_ga96c59c754178451d8dbd08b32813220b"></a>

```c
enum hawkbit_response { HAWKBIT_NO_RESPONSE , HAWKBIT_UPDATE_INSTALLED , HAWKBIT_NO_UPDATE , HAWKBIT_NETWORKING_ERROR , HAWKBIT_UNCONFIRMED_IMAGE , HAWKBIT_PERMISSION_ERROR , HAWKBIT_METADATA_ERROR , HAWKBIT_DOWNLOAD_ERROR , HAWKBIT_ALLOC_ERROR , HAWKBIT_NOT_INITIALIZED , HAWKBIT_PROBE_IN_PROGRESS }
```

相关声明：[hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)、[HAWKBIT_NO_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9)、[HAWKBIT_UPDATE_INSTALLED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048)、[HAWKBIT_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71)、[HAWKBIT_NETWORKING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8)、[HAWKBIT_UNCONFIRMED_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d)、[HAWKBIT_PERMISSION_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124)、[HAWKBIT_METADATA_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a)、[HAWKBIT_DOWNLOAD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9)、[HAWKBIT_ALLOC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01)、[HAWKBIT_NOT_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708)、[HAWKBIT_PROBE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)。

hawkBit 返回的响应消息（Response Message）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.3\_函数（Functions）

<a id="r_gad8e83255a969eb61244b1edfd0b95e5d"></a>

```c
int hawkbit_set_custom_data_cb (hawkbit_config_device_data_cb_handler_t cb)
```

相关声明：[hawkbit_set_custom_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gad8e83255a969eb61244b1edfd0b95e5d)、[hawkbit_config_device_data_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga2774769ec44f2793895b5d783b4dceda)。

设置自定义数据回调（Custom Data Callback）。

<a id="r_ga0ef6151f205088405de242e012984ca6"></a>

```c
int hawkbit_init (void)
```

相关声明：[hawkbit_init](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga0ef6151f205088405de242e012984ca6)。

初始化闪存分区（Flash Partition）。

<a id="r_ga525173f0c3d0ca4e26124a34d098d0b9"></a>

```c
enum hawkbit_response hawkbit_probe (void)
```

相关声明：[hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)、[hawkbit_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga525173f0c3d0ca4e26124a34d098d0b9)。

hawkBit 探测（Probe）用于检查是否有需要执行的更新。

<a id="r_ga03631b12a4107d660bac14bfd33bfebd"></a>

```c
void hawkbit_reboot (void)
```

相关声明：[hawkbit_reboot](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga03631b12a4107d660bac14bfd33bfebd)。

请求系统重新启动（reboot）。

<a id="r_ga4ce085b8f2bb46af2c2e9f3f2879d633"></a>

```c
int hawkbit_set_device_identity_cb (hawkbit_get_device_identity_cb_handler_t cb)
```

相关声明：[hawkbit_set_device_identity_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga4ce085b8f2bb46af2c2e9f3f2879d633)、[hawkbit_get_device_identity_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga154220c632a7594c0630cdcd79385055)。

设置设备身份回调（Device Identity Callback）。

<a id="r_ga26f0066c87c57b500170ac377b560bb4"></a>

```c
int hawkbit_reset_action_id (void)
```

相关声明：[hawkbit_reset_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga26f0066c87c57b500170ac377b560bb4)。

重置保存在设置（Settings）中的 hawkBit 操作标识（Action ID）。


## 24.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P307_hawkbit.h_源码浏览.md)
- [hawkbit_config_device_data_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga2774769ec44f2793895b5d783b4dceda)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [hawkbit_get_device_identity_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga154220c632a7594c0630cdcd79385055)
- [hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)
- [HAWKBIT_NO_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9)
- [HAWKBIT_UPDATE_INSTALLED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048)
- [HAWKBIT_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71)
- [HAWKBIT_NETWORKING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8)
- [HAWKBIT_UNCONFIRMED_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d)
- [HAWKBIT_PERMISSION_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124)
- [HAWKBIT_METADATA_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a)
- [HAWKBIT_DOWNLOAD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9)
- [HAWKBIT_ALLOC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01)
- [HAWKBIT_NOT_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708)
- [HAWKBIT_PROBE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)
- [hawkbit_set_custom_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gad8e83255a969eb61244b1edfd0b95e5d)
- [hawkbit_init](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga0ef6151f205088405de242e012984ca6)
- [hawkbit_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga525173f0c3d0ca4e26124a34d098d0b9)
- [hawkbit_reboot](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga03631b12a4107d660bac14bfd33bfebd)
- [hawkbit_set_device_identity_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga4ce085b8f2bb46af2c2e9f3f2879d633)
- [hawkbit_reset_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga26f0066c87c57b500170ac377b560bb4)

<a id="header-details"></a>

---

[上一章](P023_zephyr__drivers__gpio__gpio_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__bluetooth__classic__hid_device.h_文件参考.md)
