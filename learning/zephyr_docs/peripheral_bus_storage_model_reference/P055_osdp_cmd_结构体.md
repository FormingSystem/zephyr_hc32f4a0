---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-55
title: osdp_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_osdp\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

开放监控设备协议（OSDP）的命令结构。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

开放式受监控设备协议（Open Supervised Device Protocol，OSDP）命令结构体。这是所有单独 OSDP 命令的封装。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a47c50d8c39cd47a7ad282dc91c4e9da8"></a>

```c
enum osdp_cmd_e id
```

相关声明：[osdp_cmd_e](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#abd8555e895d9370da1400f76c931ba21)、[id](#a47c50d8c39cd47a7ad282dc91c4e9da8)。

命令标识符（Command ID）。

```c
union {
```

<a id="r_a136fee991552a70e446bccc3fcbbc2a6"></a>

```c
struct osdp_cmd_led led
```

相关声明：[osdp_cmd_led](P059_osdp_cmd_led_结构体.md)、[led](#acc408da549c0ef9a83e5a569b64dcb36)。

LED 命令结构体。

<a id="r_a9af47510ebabb05211fee95ccec7d335"></a>

```c
struct osdp_cmd_buzzer buzzer
```

相关声明：[osdp_cmd_buzzer](P056_osdp_cmd_buzzer_结构体.md)、[buzzer](#a62250f899e17c6fd94a1629f5ef9a479)。

蜂鸣器（Buzzer）命令结构体。

<a id="r_aefef189ff2f5b31f3667ccc061c156cf"></a>

```c
struct osdp_cmd_text text
```

相关声明：[osdp_cmd_text](P062_osdp_cmd_text_结构体.md)、[text](#a70630f6a8fbebacc27d889dec52336c8)。

文本（Text）命令结构体。

<a id="r_ab7a538aea4f234f5448eeac97bc1924b"></a>

```c
struct osdp_cmd_output output
```

相关声明：[osdp_cmd_output](P061_osdp_cmd_output_结构体.md)、[output](#aa745b1efadce9bc41e7253b76bdf2adf)。

输出（Output）命令结构体。

<a id="r_adc1f6f6a5d1bb282b2d87e1006b8d15b"></a>

```c
struct osdp_cmd_comset comset
```

相关声明：[osdp_cmd_comset](P057_osdp_cmd_comset_结构体.md)、[comset](#a54d63398e914cd41567288f0da456e11)。

通信设置（Comset）命令结构体。

<a id="r_afa1ff831cbab092d3ad8451af1b4801e"></a>

```c
struct osdp_cmd_keyset keyset
```

相关声明：[osdp_cmd_keyset](P058_osdp_cmd_keyset_结构体.md)、[keyset](#ad629c2622377800a0deab60756fa35a4)。

密钥设置（Keyset）命令结构体。

<a id="r_a706e31fbf66538a82d137676df0acc75"></a>

```c
};
```

命令（Command）。

## 55.2\_详细说明（Detailed Documentation）

<a id="a706e31fbf66538a82d137676df0acc75"></a>

### `[union]`

```c
union { ... } osdp_cmd
```

命令（Command）。

<a id="a62250f899e17c6fd94a1629f5ef9a479"></a>

### `buzzer`

```c
struct osdp_cmd_buzzer osdp_cmd::buzzer
```

蜂鸣器（Buzzer）命令结构体。

<a id="a54d63398e914cd41567288f0da456e11"></a>

### `comset`

```c
struct osdp_cmd_comset osdp_cmd::comset
```

通信设置（Comset）命令结构体。

<a id="a47c50d8c39cd47a7ad282dc91c4e9da8"></a>

### `id`

```c
enum osdp_cmd_e osdp_cmd::id
```

命令标识符（Command ID）。

用于选择联合体中的具体命令。

<a id="ad629c2622377800a0deab60756fa35a4"></a>

### `keyset`

```c
struct osdp_cmd_keyset osdp_cmd::keyset
```

密钥设置（Keyset）命令结构体。

<a id="acc408da549c0ef9a83e5a569b64dcb36"></a>

### `led`

```c
struct osdp_cmd_led osdp_cmd::led
```

LED 命令结构体。

<a id="aa745b1efadce9bc41e7253b76bdf2adf"></a>

### `output`

```c
struct osdp_cmd_output osdp_cmd::output
```

输出（Output）命令结构体。

<a id="a70630f6a8fbebacc27d889dec52336c8"></a>

### `text`

```c
struct osdp_cmd_text osdp_cmd::text
```

文本（Text）命令结构体。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [osdp_cmd_e](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h.html#abd8555e895d9370da1400f76c931ba21)
- [osdp_cmd_led](P059_osdp_cmd_led_结构体.md)
- [osdp_cmd_buzzer](P056_osdp_cmd_buzzer_结构体.md)
- [osdp_cmd_text](P062_osdp_cmd_text_结构体.md)
- [osdp_cmd_output](P061_osdp_cmd_output_结构体.md)
- [osdp_cmd_comset](P057_osdp_cmd_comset_结构体.md)
- [osdp_cmd_keyset](P058_osdp_cmd_keyset_结构体.md)
- [osdp_cmd](P055_osdp_cmd_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_mux_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_osdp_cmd_buzzer_结构体.md)
