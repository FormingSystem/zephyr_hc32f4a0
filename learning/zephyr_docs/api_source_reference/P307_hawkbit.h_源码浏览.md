---
id: learning.zephyr-docs.api-source-reference.page-307
title: hawkbit.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第307章\_hawkbit.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)。

## 307.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="agroup__hawkbit_html_ga03631b12a4107d660bac14bfd33bfebd"></a>
<a id="agroup__hawkbit_html_ga0ef6151f205088405de242e012984ca6"></a>
<a id="agroup__hawkbit_html_ga154220c632a7594c0630cdcd79385055"></a>
<a id="agroup__hawkbit_html_ga26f0066c87c57b500170ac377b560bb4"></a>
<a id="agroup__hawkbit_html_ga2774769ec44f2793895b5d783b4dceda"></a>
<a id="agroup__hawkbit_html_ga4ce085b8f2bb46af2c2e9f3f2879d633"></a>
<a id="agroup__hawkbit_html_ga525173f0c3d0ca4e26124a34d098d0b9"></a>
<a id="agroup__hawkbit_html_ga96c59c754178451d8dbd08b32813220b"></a>
<a id="agroup__hawkbit_html_gad8e83255a969eb61244b1edfd0b95e5d"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220baa18639f74548a317808b24c702f2fcb9"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220bacee282923e7435b81794ccec9749ce01"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d"></a>
<a id="agroup__hawkbit_html_gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2020 Linumiz
 * Copyright (c) 2024 Vogl Electronic GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_MGMT_HAWKBIT_HAWKBIT_H_
#define ZEPHYR_INCLUDE_MGMT_HAWKBIT_HAWKBIT_H_

#include <stdint.h>

enum hawkbit_response {
        HAWKBIT_NO_RESPONSE,
        HAWKBIT_UPDATE_INSTALLED,
        HAWKBIT_NO_UPDATE,
        HAWKBIT_NETWORKING_ERROR,
        HAWKBIT_UNCONFIRMED_IMAGE,
        HAWKBIT_PERMISSION_ERROR,
        HAWKBIT_METADATA_ERROR,
        HAWKBIT_DOWNLOAD_ERROR,
        HAWKBIT_ALLOC_ERROR,
        HAWKBIT_NOT_INITIALIZED,
        HAWKBIT_PROBE_IN_PROGRESS,
};

typedef int (*hawkbit_config_device_data_cb_handler_t)(const char *device_id, uint8_t *buffer,
                                                  const size_t buffer_size);

int hawkbit_set_custom_data_cb(hawkbit_config_device_data_cb_handler_t cb);

int hawkbit_init(void);

enum hawkbit_response hawkbit_probe(void);

void hawkbit_reboot(void);

typedef bool (*hawkbit_get_device_identity_cb_handler_t)(char *id, int id_max_len);

int hawkbit_set_device_identity_cb(hawkbit_get_device_identity_cb_handler_t cb);

int hawkbit_reset_action_id(void);


#endif /* ZEPHYR_INCLUDE_MGMT_HAWKBIT_HAWKBIT_H_ */
```

## 307.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Linumiz。

版权（Copyright）：© 2024 Vogl Electronic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 142 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_HAWKBIT_HAWKBIT_H_`。

## 307.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hawkbit_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
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
- [hawkbit_config_device_data_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga2774769ec44f2793895b5d783b4dceda)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hawkbit_set_custom_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gad8e83255a969eb61244b1edfd0b95e5d)
- [hawkbit_init](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga0ef6151f205088405de242e012984ca6)
- [hawkbit_probe](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga525173f0c3d0ca4e26124a34d098d0b9)
- [hawkbit_reboot](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga03631b12a4107d660bac14bfd33bfebd)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [hawkbit_get_device_identity_cb_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga154220c632a7594c0630cdcd79385055)
- [hawkbit_set_device_identity_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga4ce085b8f2bb46af2c2e9f3f2879d633)
- [hawkbit_reset_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga26f0066c87c57b500170ac377b560bb4)

---

[上一章](P306_has.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P308_hci_driver_bluenrg.h_源码浏览.md)
