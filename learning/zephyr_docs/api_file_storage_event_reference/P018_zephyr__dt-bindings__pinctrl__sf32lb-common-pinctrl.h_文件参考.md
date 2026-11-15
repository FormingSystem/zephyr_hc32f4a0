---
id: learning.zephyr-docs.api-file-storage-event-reference.page-18
title: zephyr__dt-bindings__pinctrl__sf32lb-common-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_sf32lb-common-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="r_a5646f0c724cca9d2b172dfc1f688396d"></a>

```c
#define SF32LB_FSEL_POS 0U
```

相关声明：[SF32LB_FSEL_POS](#a5646f0c724cca9d2b172dfc1f688396d)。

<a id="r_a04282baed892f488e9e3115903b0b50a"></a>

```c
#define SF32LB_FSEL_MSK 0x0000000FU
```

相关声明：[SF32LB_FSEL_MSK](#a04282baed892f488e9e3115903b0b50a)。

<a id="r_a77728f97cef4eb0d45df16a38434d13a"></a>

```c
#define SF32LB_PORT_POS 12U
```

相关声明：[SF32LB_PORT_POS](#a77728f97cef4eb0d45df16a38434d13a)。

<a id="r_aafaf655024a4ad54ad20860f2a19f81f"></a>

```c
#define SF32LB_PORT_MSK 0x00003000U
```

相关声明：[SF32LB_PORT_MSK](#aafaf655024a4ad54ad20860f2a19f81f)。

<a id="r_add6a07098f4280615c40a96c920b77f1"></a>

```c
#define SF32LB_PAD_POS 14U
```

相关声明：[SF32LB_PAD_POS](#add6a07098f4280615c40a96c920b77f1)。

<a id="r_a74ba967ed16400f6cf2acc0713aef3bd"></a>

```c
#define SF32LB_PAD_MSK 0x003FC000U
```

相关声明：[SF32LB_PAD_MSK](#a74ba967ed16400f6cf2acc0713aef3bd)。

<a id="r_a405be27c1882da2d8cccdc4ef2e6d7c1"></a>

```c
#define SF32LB_PINR_FIELD_POS 22U
```

相关声明：[SF32LB_PINR_FIELD_POS](#a405be27c1882da2d8cccdc4ef2e6d7c1)。

<a id="r_a6ab4bd9b0603e58c5db48dadf3ee0678"></a>

```c
#define SF32LB_PINR_FIELD_MSK 0x00C00000U
```

相关声明：[SF32LB_PINR_FIELD_MSK](#a6ab4bd9b0603e58c5db48dadf3ee0678)。

<a id="r_a1b29817b97463406fd25a378398f86a8"></a>

```c
#define SF32LB_PINR_OFFSET_POS 24U
```

相关声明：[SF32LB_PINR_OFFSET_POS](#a1b29817b97463406fd25a378398f86a8)。

<a id="r_acc7fdb3027e28ad8db430a177c958b5d"></a>

```c
#define SF32LB_PINR_OFFSET_MSK 0xFF000000U
```

相关声明：[SF32LB_PINR_OFFSET_MSK](#acc7fdb3027e28ad8db430a177c958b5d)。

<a id="r_ae5455da62c21d609d50622d403964781"></a>

```c
#define SF32LB_PINMUX(port, pad, fsel, pinr_offset, pinr_field)
```

相关声明：[SF32LB_PINMUX](#ae5455da62c21d609d50622d403964781)。

引脚配置位域（Pin Configuration Bit Field）。

<a id="r_a550d807fda96c8c76629513159a317b3"></a>

```c
#define SF32LB_PINMUX_ANALOG(port, pad)
```

相关声明：[SF32LB_PINMUX_ANALOG](#a550d807fda96c8c76629513159a317b3)。

模拟模式引脚配置（Analog Mode Pin Configuration）。

## 18.2\_详细说明（Detailed Documentation）

<a id="a04282baed892f488e9e3115903b0b50a"></a>

### `SF32LB_FSEL_MSK`

```c
#define SF32LB_FSEL_MSK 0x0000000FU
```

<a id="a5646f0c724cca9d2b172dfc1f688396d"></a>

### `SF32LB_FSEL_POS`

```c
#define SF32LB_FSEL_POS 0U
```

<a id="a74ba967ed16400f6cf2acc0713aef3bd"></a>

### `SF32LB_PAD_MSK`

```c
#define SF32LB_PAD_MSK 0x003FC000U
```

<a id="add6a07098f4280615c40a96c920b77f1"></a>

### `SF32LB_PAD_POS`

```c
#define SF32LB_PAD_POS 14U
```

<a id="ae5455da62c21d609d50622d403964781"></a>

### `SF32LB_PINMUX`

```c
#define SF32LB_PINMUX ( port, pad, fsel, pinr_offset, pinr_field )
```

展开值（Value）：

```c
((((pinr_offset) << SF32LB_PINR_OFFSET_POS) & SF32LB_PINR_OFFSET_MSK) |                    \
 (((pinr_field) << SF32LB_PINR_FIELD_POS) & SF32LB_PINR_FIELD_MSK) |                       \
 (((SF32LB_PORT_##port) << SF32LB_PORT_POS) & SF32LB_PORT_MSK) |                           \
 (((pad) << SF32LB_PAD_POS) & SF32LB_PAD_MSK) |                                            \
 (((fsel) << SF32LB_FSEL_POS) & SF32LB_FSEL_MSK))
```

引脚配置位域（Pin Configuration Bit Field）。

位图（Bitmap）：

- 位 `0–10`：配置位（Configuration Bits），包括功能选择、上下拉、驱动强度等。
- 位 `11`：保留（Reserved）。
- 位 `12–13`：端口（Port），如 SA、PA 等。
- 位 `14–21`：焊盘（Pad），范围 `0–128`。
- 位 `22–23`：PINR 寄存器字段（Register Field），范围 `0–3`。
- 位 `24–31`：PINR 寄存器偏移量（Register Offset），范围 `1–255`，`0` 表示未使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port）。 |
| `pad` | 连接端口（Pad） |
| `fsel` | 功能选择（Function Select）。 |
| `pinr_offset` | PINR 寄存器偏移量（Register Offset）。 |
| `pinr_field` | PINR 寄存器字段（Register Field）。 |

<a id="a550d807fda96c8c76629513159a317b3"></a>

### `SF32LB_PINMUX_ANALOG`

```c
#define SF32LB_PINMUX_ANALOG ( port, pad )
```

展开值（Value）：

```c
((((SF32LB_PORT_##port) << SF32LB_PORT_POS) & SF32LB_PORT_MSK) |                           \
 (((pad) << SF32LB_PAD_POS) & SF32LB_PAD_MSK) |                                            \
 ((15U << SF32LB_FSEL_POS) & SF32LB_FSEL_MSK))
```

模拟模式引脚配置（Analog Mode Pin Configuration）。

将引脚配置为模拟模式（Analog Mode）：`FSEL=15`、`PE=0`（禁用上下拉）、`IE=0`（禁用输入）。用于 ADC 输入、电源引脚或其他模拟功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port），如 SA、PA 等。 |
| `pad` | 焊盘编号（Pad Number）。 |

<a id="a6ab4bd9b0603e58c5db48dadf3ee0678"></a>

### `SF32LB_PINR_FIELD_MSK`

```c
#define SF32LB_PINR_FIELD_MSK 0x00C00000U
```

<a id="a405be27c1882da2d8cccdc4ef2e6d7c1"></a>

### `SF32LB_PINR_FIELD_POS`

```c
#define SF32LB_PINR_FIELD_POS 22U
```

<a id="acc7fdb3027e28ad8db430a177c958b5d"></a>

### `SF32LB_PINR_OFFSET_MSK`

```c
#define SF32LB_PINR_OFFSET_MSK 0xFF000000U
```

<a id="a1b29817b97463406fd25a378398f86a8"></a>

### `SF32LB_PINR_OFFSET_POS`

```c
#define SF32LB_PINR_OFFSET_POS 24U
```

<a id="aafaf655024a4ad54ad20860f2a19f81f"></a>

### `SF32LB_PORT_MSK`

```c
#define SF32LB_PORT_MSK 0x00003000U
```

<a id="a77728f97cef4eb0d45df16a38434d13a"></a>

### `SF32LB_PORT_POS`

```c
#define SF32LB_PORT_POS 12U
```


## 18.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P774_sf32lb-common-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asf32lb-common-pinctrl_8h_html_a04282baed892f488e9e3115903b0b50a"></a>
<a id="asf32lb-common-pinctrl_8h_html_a1b29817b97463406fd25a378398f86a8"></a>
<a id="asf32lb-common-pinctrl_8h_html_a405be27c1882da2d8cccdc4ef2e6d7c1"></a>
<a id="asf32lb-common-pinctrl_8h_html_a5646f0c724cca9d2b172dfc1f688396d"></a>
<a id="asf32lb-common-pinctrl_8h_html_a6ab4bd9b0603e58c5db48dadf3ee0678"></a>
<a id="asf32lb-common-pinctrl_8h_html_a74ba967ed16400f6cf2acc0713aef3bd"></a>
<a id="asf32lb-common-pinctrl_8h_html_a77728f97cef4eb0d45df16a38434d13a"></a>
<a id="asf32lb-common-pinctrl_8h_html_aafaf655024a4ad54ad20860f2a19f81f"></a>
<a id="asf32lb-common-pinctrl_8h_html_acc7fdb3027e28ad8db430a177c958b5d"></a>
<a id="asf32lb-common-pinctrl_8h_html_add6a07098f4280615c40a96c920b77f1"></a>

---

[上一章](P017_zephyr__sensing__sensing.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__stepper__stepper.h_文件参考.md)
