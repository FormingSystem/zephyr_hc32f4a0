---
id: learning.zephyr-docs.api-protocol-topic-reference.page-59
title: Wi-Fi 扫描配置（Scanning configuration）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__wscan__configuration.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_Wi-Fi 扫描配置（Scanning configuration）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__wscan__configuration.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 59.1\_宏定义（Macros）

<a id="r_gac67a00c5b9b85afbb2c76a3b44d04f9d"></a>

```c
#define URC_MODE 1
```

相关声明：[URC_MODE](#gac67a00c5b9b85afbb2c76a3b44d04f9d)。

为避免 UART 反复传输过多数据，主机（Host）可设置筛选模式（filter mode），使整个 Wi-Fi 扫描期间发现的每个基本服务集标识符（BSSID）仅显示一次。

<a id="r_ga9e38942a920e3dbb9101c0388fdf137d"></a>

```c
#define HOPPING_TIME 1024
```

相关声明：[HOPPING_TIME](#ga9e38942a920e3dbb9101c0388fdf137d)。

跳频时间（hopping time）指切换到下一个信道之前的扫描时长，单位为毫秒。

<a id="r_ga468e1c5d4d85203d0d644dd0e022dec3"></a>

```c
#define ANT_SEL 1
```

相关声明：[ANT_SEL](#ga468e1c5d4d85203d0d644dd0e022dec3)。

为天线选择合适的 ST87 输入端：全球导航卫星系统（GNSS）或窄带物联网（NB-IoT）。

## 59.2\_详细说明（Detailed Documentation）

<a id="ga468e1c5d4d85203d0d644dd0e022dec3"></a>

### `ANT_SEL`

```c
#define ANT_SEL 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

为天线选择合适的 ST87 输入端：全球导航卫星系统（GNSS）或窄带物联网（NB-IoT）。

可用值：0 为 GNSS 天线输入（默认模式）；1 为 NB-IoT 天线输入。

<a id="ga9e38942a920e3dbb9101c0388fdf137d"></a>

### `HOPPING_TIME`

```c
#define HOPPING_TIME 1024
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

跳频时间（hopping time）指切换到下一个信道之前的扫描时长，单位为毫秒。

<a id="gac67a00c5b9b85afbb2c76a3b44d04f9d"></a>

### `URC_MODE`

```c
#define URC_MODE 1
```

```c
#include <zephyr/drivers/modem/st87mxx_app_services.h>
```

为避免 UART 反复传输过多数据，主机（Host）可设置筛选模式（filter mode），使整个 Wi-Fi 扫描期间发现的每个基本服务集标识符（BSSID）仅显示一次。

可用值：0 表示一轮后仅报告新服务集标识符（SSID），为默认模式；1 表示在无限循环中输出非请求结果码（URC）。


## 59.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/st87mxx_app_services.h](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P058_SNTP 服务器.md) · [返回大纲](大纲.md) · [下一章](P060_STM32 SDMMC API主题.md)
