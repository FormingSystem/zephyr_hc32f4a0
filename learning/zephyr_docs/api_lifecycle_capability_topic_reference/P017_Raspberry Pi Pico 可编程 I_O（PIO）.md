---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-17
title: Raspberry Pi Pico 可编程 I_O（PIO）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_Raspberry Pi Pico 可编程 I\_O（PIO）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pio__rpi__pico__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Raspberry Pi Pico 可编程 I/O（Programmable I/O，PIO）接口。

<a id="details"></a>

Raspberry Pi Pico 可编程 I/O（Programmable I/O，PIO）接口。

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_pio_5Frpi_5Fpico_2Eh"></a>

```c
file pio_rpi_pico.h
```

相关声明：[pio_rpi_pico.h](../api_file_service_interface_reference/P042_zephyr__drivers__misc__pio_rpi_pico__pio_rpi_pico.h_文件参考.md)。

Raspberry Pi Pico可编程输入输出（PIO）驱动的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_ga744449bb6c1a409a9d8677c66667ea9b"></a>

```c
#define RPI_PICO_PIO_DEFINE_PROGRAM(name, wrap_target, wrap, ...)
```

相关声明：[RPI_PICO_PIO_DEFINE_PROGRAM](#ga744449bb6c1a409a9d8677c66667ea9b)。

定义可编程输入输出（PIO）程序的辅助宏（Utility Macro）。

<a id="r_ga0d74a21471e301563224d4673ca1a738"></a>

```c
#define RPI_PICO_PIO_GET_WRAP_TARGET(name)
```

相关声明：[RPI_PICO_PIO_GET_WRAP_TARGET](#ga0d74a21471e301563224d4673ca1a738)。

获取程序回绕目标（Wrap Target）的辅助宏（Utility Macro）。

<a id="r_ga5cc3f015332a73cba6141e94b8fbe67e"></a>

```c
#define RPI_PICO_PIO_GET_WRAP(name)
```

相关声明：[RPI_PICO_PIO_GET_WRAP](#ga5cc3f015332a73cba6141e94b8fbe67e)。

获取程序回绕源（Wrap Source）的辅助宏（Utility Macro）。

<a id="r_ga989341427ba2e681aba5c4d702d91927"></a>

```c
#define RPI_PICO_PIO_GET_PROGRAM(name)
```

相关声明：[RPI_PICO_PIO_GET_PROGRAM](#ga989341427ba2e681aba5c4d702d91927)。

获取 PIO 程序指针的辅助宏（Utility Macro）。

<a id="r_ga482acc1e13f4b6ef96f55a2c9e3b7a07"></a>

```c
#define DT_RPI_PICO_PIO_PIN_BY_NAME(node_id, p_name, p_idx, g_name, g_idx)
```

相关声明：[DT_RPI_PICO_PIO_PIN_BY_NAME](#ga482acc1e13f4b6ef96f55a2c9e3b7a07)。

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

<a id="r_gaa3620b14a4d34eed3302048d58a86893"></a>

```c
#define DT_INST_RPI_PICO_PIO_PIN_BY_NAME(inst, p_name, p_idx, g_name, g_idx)
```

相关声明：[DT_INST_RPI_PICO_PIO_PIN_BY_NAME](#gaa3620b14a4d34eed3302048d58a86893)。

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

<a id="r_gad2aef23ab08361004bba9209f9e612c1"></a>

```c
#define DT_INST_PIO_PIN_BY_NAME(inst, name)
```

相关声明：[DT_INST_PIO_PIN_BY_NAME](#gad2aef23ab08361004bba9209f9e612c1)。

根据引脚名称获取引脚编号（Pin Number）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_gad9607572a90350fc3c6cf818e3efa99a"></a>

```c
static PIO pio_rpi_pico_get_pio (const struct device *dev)
```

相关声明：[pio_rpi_pico_get_pio](#gad9607572a90350fc3c6cf818e3efa99a)、[device](../device_reference/P002_设备对象结构.md)。

获取可编程输入输出（PIO）对象。

<a id="r_gac3c70836b493b3fd535ea073c1f7d55b"></a>

```c
int pio_rpi_pico_allocate_sm (const struct device *dev, size_t *sm)
```

相关声明：[pio_rpi_pico_allocate_sm](#gac3c70836b493b3fd535ea073c1f7d55b)、[device](../device_reference/P002_设备对象结构.md)。

分配状态机（State Machine）。

## 17.4\_详细说明（Detailed Documentation）

<a id="gad2aef23ab08361004bba9209f9e612c1"></a>

### `DT_INST_PIO_PIN_BY_NAME`

```c
#define DT_INST_PIO_PIN_BY_NAME ( inst, name )
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
DT_PIO_PIN_BY_NAME(DT_DRV_INST(inst), name)
```

根据引脚名称获取引脚编号（Pin Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号。 |
| `name` | 引脚名称（Pin Name），例如 `tx`、`rx`、`sck`。 |

<a id="gaa3620b14a4d34eed3302048d58a86893"></a>

### `DT_INST_RPI_PICO_PIO_PIN_BY_NAME`

```c
#define DT_INST_RPI_PICO_PIO_PIN_BY_NAME ( inst, p_name, p_idx, g_name, g_idx )
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
DT_RPI_PICO_PIO_PIN_BY_NAME(DT_DRV_INST(inst), p_name, p_idx, g_name, g_idx)
```

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号。 |
| `p_name` | 引脚控制名称（Pinctrl Name）。 |
| `p_idx` | 引脚控制索引（Pinctrl Index）。 |
| `g_name` | 组名称（Group Name）。 |
| `g_idx` | 组索引（Group Index）。 |

**返回（Returns）**：**返回值（Returns）：**引脚编号（Pin Number）。

**参阅（See Also）**：**另见（See Also）：**`DT_RPI_PICO_PIO_PIN_BY_NAME`。

<a id="ga482acc1e13f4b6ef96f55a2c9e3b7a07"></a>

### `DT_RPI_PICO_PIO_PIN_BY_NAME`

```c
#define DT_RPI_PICO_PIO_PIN_BY_NAME ( node_id, p_name, p_idx, g_name, g_idx )
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
RP2_GET_PIN_NUM(DT_PROP_BY_IDX(                                                         \
        DT_CHILD(DT_PINCTRL_BY_NAME(node_id, p_name, p_idx), g_name), pinmux, g_idx))
```

根据引脚控制（Pinctrl）／组名称和索引获取引脚编号。

设备树片段示例（Example Devicetree Fragments）：

原始示例（Example）：

```c
pinctrl {
   pio_child_default: pio_child_default {
           tx_gpio {
                   pinmux = <PIO0_P0>, <PIO0_P2>;
           };

           rx_gpio {
                   pinmux = <PIO0_P1>;
                   input-enable;
           };
   };
};
```

原始示例（Example）：

```c
pio {
   status = "okay";
   c: child {
           pinctrl-0 = <&pio_child_default>;
           pinctrl-names = "default";
   };
};
```

使用示例：

原始示例（Example）：

```c
DT_RPI_PICO_PIO_PIN_BY_NAME(node, default, 0, tx_gpio, 0) // 0
DT_RPI_PICO_PIO_PIN_BY_NAME(node, default, 0, tx_gpio, 1) // 2
DT_RPI_PICO_PIO_PIN_BY_NAME(node, default, 0, rx_gpio, 0) // 1
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |
| `p_name` | 引脚控制名称（Pinctrl Name）。 |
| `p_idx` | 引脚控制索引（Pinctrl Index）。 |
| `g_name` | 组名称（Group Name）。 |
| `g_idx` | 组索引（Group Index）。 |

**返回（Returns）**：**返回值（Returns）：**引脚编号（Pin Number）。

<a id="ga744449bb6c1a409a9d8677c66667ea9b"></a>

### `RPI_PICO_PIO_DEFINE_PROGRAM`

```c
#define RPI_PICO_PIO_DEFINE_PROGRAM ( name, wrap_target, wrap, ... )
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
static const uint32_t name ## _wrap_target = wrap_target;       \
static const uint32_t name ## _wrap = wrap;                     \
static const uint16_t name ## _program_instructions[] = {       \
        __VA_ARGS__                                             \
};                                                              \
static const struct pio_program name ## _program = {            \
        .instructions = name ## _program_instructions,          \
        .length = ARRAY_SIZE(name ## _program_instructions),    \
        .origin = -1,                                           \
}
```

定义可编程输入输出（PIO）程序的辅助宏（Utility Macro）。

程序是由 `pioasm` 工具生成的一组 16 位指令（Instructions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 程序名称（Program Name）。 |
| `wrap_target` | PIO 程序指定的循环回跳目标（Wrap Target）。 |
| `wrap` | PIO 程序指定的循环回跳起点（Wrap Source）。 |
| `...` | 逗号分隔的 PIO 指令列表（Instructions List）。 |

<a id="ga989341427ba2e681aba5c4d702d91927"></a>

### `RPI_PICO_PIO_GET_PROGRAM`

```c
#define RPI_PICO_PIO_GET_PROGRAM ( name)
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
&name ## _program
```

获取 PIO 程序指针的辅助宏（Utility Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 程序名称（Program Name）。 |

<a id="ga5cc3f015332a73cba6141e94b8fbe67e"></a>

### `RPI_PICO_PIO_GET_WRAP`

```c
#define RPI_PICO_PIO_GET_WRAP ( name)
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
name ## _wrap
```

获取程序回绕源（Wrap Source）的辅助宏（Utility Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 程序名称（Program Name）。 |

<a id="ga0d74a21471e301563224d4673ca1a738"></a>

### `RPI_PICO_PIO_GET_WRAP_TARGET`

```c
#define RPI_PICO_PIO_GET_WRAP_TARGET ( name)
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

展开值（Value）：

```c
name ## _wrap_target
```

获取程序回绕目标（Wrap Target）的辅助宏（Utility Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 程序名称（Program Name）。 |

<a id="gac3c70836b493b3fd535ea073c1f7d55b"></a>

### `pio_rpi_pico_allocate_sm()`

```c
int pio_rpi_pico_allocate_sm ( const struct device * dev, size_t * sm )
```

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

分配状态机（State Machine）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 `rpi_pio` 设备实例的设备结构体（Device Structure）的指针。 |
| `sm` | 用于存储已分配状态机（Allocated State Machine）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 没有可用状态机（State Machines）时。 |

<a id="gad9607572a90350fc3c6cf818e3efa99a"></a>

### `pio_rpi_pico_get_pio()`

```c
PIO pio_rpi_pico_get_pio ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/pio_rpi_pico/pio_rpi_pico.h>
```

获取可编程输入输出（PIO）对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 `rpi_pio` 设备实例的设备结构体（Device Structure）的指针。 |

**返回（Returns）**：**返回值（Returns）：**PIO 对象（Object）。


## 17.5\_原页交叉引用（Cross References）

- [pio_rpi_pico.h](../api_file_service_interface_reference/P042_zephyr__drivers__misc__pio_rpi_pico__pio_rpi_pico.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)
- [DT_CHILD](../dt_identity_reference/P001_设备树节点标识宏.md#ga88259608f4e9083ccc2e9ca5ec2c212e)
- [DT_PINCTRL_BY_NAME](../pinctrl_reference/P005_引脚控制设备树宏.md#ga1cd336f902738fd684f3d81b3fb6caae)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__pio__rpi__pico__interface_html_ga482acc1e13f4b6ef96f55a2c9e3b7a07"></a>
<a id="agroup__devicetree-generic-id_html_ga88259608f4e9083ccc2e9ca5ec2c212e"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__devicetree-pinctrl_html_ga1cd336f902738fd684f3d81b3fb6caae"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_Renesas R-Car 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P018_STM32 正交解码器（QDEC STM32）.md)
