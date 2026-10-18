---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-34
title: zephyr__net__wifi_utils.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_net\_\_wifi\_utils.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi子系统（Subsystem）使用的工具函数。

<a id="details"></a>

```c
#include <zephyr/net/wifi.h>
#include <zephyr/net/wifi_mgmt.h>
```

查看此文件的源码。

Wi-Fi子系统（Subsystem）使用的工具函数。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 34.1\_Wi-Fi 工具函数（Utility Functions）

Wi-Fi 子系统（Subsystem）的工具函数（Utility Functions）。

<a id="r_ga1104c3c97b460f9f3e15a7a9c56e80af"></a>

```c
#define WIFI_UTILS_MAX_BAND_STR_LEN 3
```

相关声明：[WIFI_UTILS_MAX_BAND_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1104c3c97b460f9f3e15a7a9c56e80af)。

频段说明字符串（Band Specification String）的最大长度。

<a id="r_gaacc3c661affda7b376a4024efd645f0b"></a>

```c
#define WIFI_UTILS_MAX_CHAN_STR_LEN 4
```

相关声明：[WIFI_UTILS_MAX_CHAN_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc3c661affda7b376a4024efd645f0b)。

信道说明字符串（Channel Specification String）的最大长度。

<a id="r_ga4c91cd7dff0fd9e5402970f3222dc20d"></a>

```c
int wifi_utils_parse_scan_bands (char *scan_bands_str, uint8_t *band_map)
```

相关声明：[wifi_utils_parse_scan_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c91cd7dff0fd9e5402970f3222dc20d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将频段说明字符串（Band Specification String）转换为表示频段的位图（Bitmap）。

<a id="r_ga471a96d3fb6d610a591508b52d4c05a4"></a>

```c
int wifi_utils_parse_scan_ssids (char *scan_ssids_str, const char *ssids[], uint8_t num_ssids)
```

相关声明：[wifi_utils_parse_scan_ssids](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga471a96d3fb6d610a591508b52d4c05a4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将包含 SSID 的字符串追加到 SSID 字符串数组（String Array）。

<a id="r_gaba9f3117bcef9da1efc1841d3bd9adfd"></a>

```c
int wifi_utils_parse_scan_chan (char *scan_chan_str, struct wifi_band_channel *chan, uint8_t max_channels)
```

相关声明：[wifi_utils_parse_scan_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaba9f3117bcef9da1efc1841d3bd9adfd)、[wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将包含扫描信道说明（Scan Channel Specification）的字符串转换为数组。

<a id="r_gaf1872d0ed2efd3737a36dcc0ab13f18e"></a>

```c
bool wifi_utils_validate_chan (uint8_t band, uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1872d0ed2efd3737a36dcc0ab13f18e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据频段（Band）验证信道（Channel）。

<a id="r_gaf408ba9f75354d3eca735b4804fdf199"></a>

```c
bool wifi_utils_validate_chan_2g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_2g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf408ba9f75354d3eca735b4804fdf199)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 2.4 GHz 频段（Band）验证信道（Channel）。

<a id="r_gae013eee6d6b74126c29d6ca7b2036310"></a>

```c
bool wifi_utils_validate_chan_5g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_5g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae013eee6d6b74126c29d6ca7b2036310)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 5 GHz 频段（Band）验证信道（Channel）。

<a id="r_ga2606742e23f48da5ca1660aeac47888b"></a>

```c
bool wifi_utils_validate_chan_6g (uint16_t chan)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_utils_validate_chan_6g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2606742e23f48da5ca1660aeac47888b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

按 6 GHz 频段（Band）验证信道（Channel）。

<a id="r_ga6fb496c072323dee6f09bfa44c42685f"></a>

```c
enum wifi_frequency_bands wifi_utils_chan_to_band (uint16_t chan)
```

相关声明：[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)、[wifi_utils_chan_to_band](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fb496c072323dee6f09bfa44c42685f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取信道所属频段（Frequency Band）。

<a id="r_ga428896bb7947b4fb46bf240b5179c7a3"></a>

```c
uint16_t wifi_utils_chan_to_freq (enum wifi_frequency_bands band, uint16_t chan)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[wifi_utils_chan_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga428896bb7947b4fb46bf240b5179c7a3)、[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将信道编号（Channel Number）转换为中心频率（Center Frequency）。

<a id="r_gaa9f346e3f44ad3441813a39bef559e2a"></a>

```c
uint16_t wifi_utils_freq_to_chan (uint16_t freq)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[wifi_utils_freq_to_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa9f346e3f44ad3441813a39bef559e2a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将中心频率（Center Frequency）转换为信道编号（Channel Number）。


## 34.2\_原页交叉引用（Cross References）

- [zephyr/net/wifi.h](../api_source_runtime_reference/P067_wifi.h_源码浏览.md)
- [zephyr/net/wifi_mgmt.h](../api_source_http_wifi_reference/P009_wifi_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P920_wifi_utils.h_源码浏览.md)
- [WIFI_UTILS_MAX_BAND_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1104c3c97b460f9f3e15a7a9c56e80af)
- [WIFI_UTILS_MAX_CHAN_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc3c661affda7b376a4024efd645f0b)
- [wifi_utils_parse_scan_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c91cd7dff0fd9e5402970f3222dc20d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_utils_parse_scan_ssids](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga471a96d3fb6d610a591508b52d4c05a4)
- [wifi_utils_parse_scan_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaba9f3117bcef9da1efc1841d3bd9adfd)
- [wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [wifi_utils_validate_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1872d0ed2efd3737a36dcc0ab13f18e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_utils_validate_chan_2g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf408ba9f75354d3eca735b4804fdf199)
- [wifi_utils_validate_chan_5g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae013eee6d6b74126c29d6ca7b2036310)
- [wifi_utils_validate_chan_6g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2606742e23f48da5ca1660aeac47888b)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [wifi_utils_chan_to_band](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fb496c072323dee6f09bfa44c42685f)
- [wifi_utils_chan_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga428896bb7947b4fb46bf240b5179c7a3)
- [wifi_utils_freq_to_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa9f346e3f44ad3441813a39bef559e2a)

<a id="header-details"></a>

---

[上一章](P033_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_capture.h_文件参考.md) · [返回大纲](大纲.md)
