---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-18
title: 全球导航卫星系统（GNSS）配置
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__gnss__configuration.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_全球导航卫星系统（GNSS）配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__gnss__configuration.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="r_gae9e5cd8119ca22dcfca38e80eb9e67b5"></a>

```c
#define GNSS_NB_MAX_POSITION 100
```

相关声明：[GNSS_NB_MAX_POSITION](#gae9e5cd8119ca22dcfca38e80eb9e67b5)。

采样位置（Sample Position）数量上限。

<a id="r_gac8b2c26a1f22ddd6c86c711440705fc0"></a>

```c
#define GNSS_CONSTELLATION_ID 0
```

相关声明：[GNSS_CONSTELLATION_ID](#gac8b2c26a1f22ddd6c86c711440705fc0)。

GNSS 星座选择（Constellation Selection）：`0` 为 GPS，`1` 为 GALLILEO，`2` 为 GPS+GALLILEO。原文将 Galileo 拼作 `GALLILEO`。

<a id="r_ga1afd16e81b65c2e7a4fa55aa0895d542"></a>

```c
#define GNSS_FORMAT_TYPE 0
```

相关声明：[GNSS_FORMAT_TYPE](#ga1afd16e81b65c2e7a4fa55aa0895d542)。

GNSS 数据格式选择（Data Format Selection）：`0` 为 ST_AT，`1` 为 NMEA。

<a id="r_gac44b0f5695f8e52c6180814794df0966"></a>

```c
#define GNSS_FORMAT_ST_POSITION 1
```

相关声明：[GNSS_FORMAT_ST_POSITION](#gac44b0f5695f8e52c6180814794df0966)。

为 GNSS 启用 ST_AT 格式时使用的参数（Parameters）。

<a id="r_ga278ff798327ebe4a97f5f40a94bdd19e"></a>

```c
#define GNSS_FORMAT_ST_ACCURACY 0
```

相关声明：[GNSS_FORMAT_ST_ACCURACY](#ga278ff798327ebe4a97f5f40a94bdd19e)。

精度数据（Accuracy Data）。

<a id="r_gae58c597d5bdfdca7d2d7364166d3dfb9"></a>

```c
#define GNSS_FORMAT_ST_SATELLITES 0
```

相关声明：[GNSS_FORMAT_ST_SATELLITES](#gae58c597d5bdfdca7d2d7364166d3dfb9)。

卫星信息（Satellites Info）。

<a id="r_ga52795780fd3c29a7bcf3578f5c68dc51"></a>

```c
#define GNSS_FORMAT_ST_ORIENTATION 0
```

相关声明：[GNSS_FORMAT_ST_ORIENTATION](#ga52795780fd3c29a7bcf3578f5c68dc51)。

方位信息（Orientation Info）。

<a id="r_ga88310315fe7e1af0a79b2ecf96c58695"></a>

```c
#define GNSS_NMEA_GPGGA 1
```

相关声明：[GNSS_NMEA_GPGGA](#ga88310315fe7e1af0a79b2ecf96c58695)。

为 GNSS 启用 NMEA 格式时使用的参数（Parameters）。

<a id="r_gae9e75d7eddd291e5bf44e73196f7214e"></a>

```c
#define GNSS_NMEA_GPGSA 0
```

相关声明：[GNSS_NMEA_GPGSA](#gae9e75d7eddd291e5bf44e73196f7214e)。

`$GPGSA` 语句信息（Info）。

<a id="r_gae9089b6e0aafd2f90510267771d84421"></a>

```c
#define GNSS_NMEA_GPGSV 0
```

相关声明：[GNSS_NMEA_GPGSV](#gae9089b6e0aafd2f90510267771d84421)。

`$GPGSV` 语句信息（Info）。

<a id="r_ga92c0f36c2f84bd0d6e43e6bcc3363b20"></a>

```c
#define GNSS_NMEA_GPGLL 1
```

相关声明：[GNSS_NMEA_GPGLL](#ga92c0f36c2f84bd0d6e43e6bcc3363b20)。

`$GPGLL` 语句信息（Info）。

<a id="r_ga107dac8cf6c95dad3e924e0275dfca9a"></a>

```c
#define GNSS_NMEA_GPRMC 0
```

相关声明：[GNSS_NMEA_GPRMC](#ga107dac8cf6c95dad3e924e0275dfca9a)。

`$GPRMS` 语句信息（Info）。

<a id="r_ga3d8409b1a22446f3926589e15d73db25"></a>

```c
#define GNSS_NMEA_GPVTG 1
```

相关声明：[GNSS_NMEA_GPVTG](#ga3d8409b1a22446f3926589e15d73db25)。

`$GPVTG` 语句信息（Info）。

## 18.2\_详细说明（Detailed Documentation）

<a id="gac8b2c26a1f22ddd6c86c711440705fc0"></a>

### `GNSS_CONSTELLATION_ID`

```c
#define GNSS_CONSTELLATION_ID 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

GNSS 星座选择（Constellation Selection）：`0` 为 GPS，`1` 为 GALLILEO，`2` 为 GPS+GALLILEO。原文将 Galileo 拼作 `GALLILEO`。

<a id="ga278ff798327ebe4a97f5f40a94bdd19e"></a>

### `GNSS_FORMAT_ST_ACCURACY`

```c
#define GNSS_FORMAT_ST_ACCURACY 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

精度数据（Accuracy Data）。

<a id="ga52795780fd3c29a7bcf3578f5c68dc51"></a>

### `GNSS_FORMAT_ST_ORIENTATION`

```c
#define GNSS_FORMAT_ST_ORIENTATION 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

方位信息（Orientation Info）。

<a id="gac44b0f5695f8e52c6180814794df0966"></a>

### `GNSS_FORMAT_ST_POSITION`

```c
#define GNSS_FORMAT_ST_POSITION 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

为 GNSS 启用 ST_AT 格式时使用的参数（Parameters）。

位置数据（Position Data）。

<a id="gae58c597d5bdfdca7d2d7364166d3dfb9"></a>

### `GNSS_FORMAT_ST_SATELLITES`

```c
#define GNSS_FORMAT_ST_SATELLITES 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

卫星信息（Satellites Info）。

<a id="ga1afd16e81b65c2e7a4fa55aa0895d542"></a>

### `GNSS_FORMAT_TYPE`

```c
#define GNSS_FORMAT_TYPE 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

GNSS 数据格式选择（Data Format Selection）：`0` 为 ST_AT，`1` 为 NMEA。

<a id="gae9e5cd8119ca22dcfca38e80eb9e67b5"></a>

### `GNSS_NB_MAX_POSITION`

```c
#define GNSS_NB_MAX_POSITION 100
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

采样位置（Sample Position）数量上限。

<a id="ga88310315fe7e1af0a79b2ecf96c58695"></a>

### `GNSS_NMEA_GPGGA`

```c
#define GNSS_NMEA_GPGGA 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

为 GNSS 启用 NMEA 格式时使用的参数（Parameters）。

`$GPGGA` 语句信息（Info）。

<a id="ga92c0f36c2f84bd0d6e43e6bcc3363b20"></a>

### `GNSS_NMEA_GPGLL`

```c
#define GNSS_NMEA_GPGLL 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

`$GPGLL` 语句信息（Info）。

<a id="gae9e75d7eddd291e5bf44e73196f7214e"></a>

### `GNSS_NMEA_GPGSA`

```c
#define GNSS_NMEA_GPGSA 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

`$GPGSA` 语句信息（Info）。

<a id="gae9089b6e0aafd2f90510267771d84421"></a>

### `GNSS_NMEA_GPGSV`

```c
#define GNSS_NMEA_GPGSV 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

`$GPGSV` 语句信息（Info）。

<a id="ga107dac8cf6c95dad3e924e0275dfca9a"></a>

### `GNSS_NMEA_GPRMC`

```c
#define GNSS_NMEA_GPRMC 0
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

`$GPRMS` 语句信息（Info）。

<a id="ga3d8409b1a22446f3926589e15d73db25"></a>

### `GNSS_NMEA_GPVTG`

```c
#define GNSS_NMEA_GPVTG 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

`$GPVTG` 语句信息（Info）。


## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/st87mxx_app_services.h](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_简单网络时间协议（SNTP）.md) · [返回大纲](大纲.md) · [下一章](P019_TMP451 API主题.md)
