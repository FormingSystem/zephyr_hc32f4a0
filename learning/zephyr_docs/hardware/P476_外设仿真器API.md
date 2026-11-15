---
id: learning.zephyr-docs.hardware.emulapi-0
title: 外设仿真器API
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第476章\_外设仿真器API

原文：[group__io__emulators](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html)。读取日期：2026-10-13，`latest`。

**仿真器（Emulator）**用于测试设备驱动以及调用驱动的上层代码。本页是设备仿真框架的**应用程序编程接口（Application Programming Interface，API）**参考：通过设备树定义实例、选择连接的总线，再初始化或取得该实例。**设备树（Devicetree，DT）**中的节点标识用于确定所仿真的设备。

## 476.1\_相关接口与结构

框架公共接口位于 `zephyr/drivers/emul.h`；`emul_stub_device.h` 为没有对应驱动的仿真器提供**桩设备（Stub Device）**支持。下面保留原页全部子主题。后端接口（Backend API）让测试程序控制仿真状态或读取结果；总线仿真接口（Bus Emulation Interface）承接被测驱动的总线操作。

| 子主题英文名 | 中文名称与用途 |
| --- | --- |
| [BBRAM emulator backend API](P490_BBRAM仿真后端接口.md) | 电池后备随机存取存储器（Battery-Backed RAM，BBRAM）仿真后端接口 |
| [BC1.2 backed emulator APIs](P491_BC1点2仿真后端接口.md) | 电池充电规范 1.2（Battery Charging 1.2，BC1.2）仿真后端接口 |
| [Biometrics emulator test helpers](P495_生物识别仿真测试接口.md) | 生物识别（Biometrics）仿真测试控制辅助函数 |
| [Emulated ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__emul.html) | 模数转换器（Analog-to-Digital Converter，ADC）仿真后端接口 |
| [Emulated GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__emul.html) | 通用输入输出（General-Purpose Input/Output，GPIO）仿真后端接口 |
| [Emulated counter](P493_计数器仿真后端接口.md) | 计数器（Counter）仿真后端接口 |
| [Fake CAN controller](https://docs.zephyrproject.org/latest/doxygen/html/group__can__fake.html) | 控制器局域网（Controller Area Network，CAN）控制器的伪实现驱动 |
| [Fake EEPROM](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__fake.html) | 电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）的伪实现驱动 |
| [Fake LED controller](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html) | 发光二极管（Light-Emitting Diode，LED）控制器的伪实现驱动 |
| [Fake PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html) | 脉宽调制（Pulse-Width Modulation，PWM）的伪实现驱动 |
| [Fake RTC](P497_RTC伪设备接口.md) | 实时时钟（Real-Time Clock，RTC）的伪实现驱动 |
| [Fake comparator](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html) | 比较器（Comparator）的伪实现驱动 |
| [Fake regulator](P498_稳压器伪设备接口.md) | 稳压器（Regulator）的伪实现驱动 |
| [Fuel gauge backend emulator APIs](P492_电量计仿真后端接口.md) | 电量计（Fuel Gauge）仿真后端接口 |
| [I2C Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html) | 集成电路间总线（Inter-Integrated Circuit，I2C）仿真接口 |
| [MSPI Emulation Interface](P487_MSPI总线仿真接口.md) | 多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）仿真接口 |
| [SPI Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html) | 串行外设接口（Serial Peripheral Interface，SPI）仿真接口 |
| [Sensor emulator backend API](P494_传感器仿真后端接口.md) | 传感器（Sensor）仿真后端接口 |
| [UART Emulation Interface](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html) | 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）仿真接口 |
| [eSPI Emulation Interface](P486_eSPI总线仿真接口.md) | 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）仿真接口 |

> 译注：原页标题 “BC1.2 backed emulator APIs” 的正文使用 “backend”，这里统一译为“后端”。Fake 表示用于测试的伪实现，名称中的器件类别仍保留英文对照。

| 数据结构 | 含义 |
| --- | --- |
| [`emul_link_for_bus`](P478_总线仿真器链接结构.md) | 唯一标识待仿真设备的结构 |
| [`emul_list_for_bus`](P479_总线仿真器列表结构.md) | 附着在一条总线上的仿真器列表 |
| [`no_bus_emul`](P480_无总线仿真器桩结构.md) | 仿真器实际没有连接总线时使用的 API 桩结构 |
| [`emul`](P477_仿真器实例结构.md) | 一个仿真器实例，表示通过仿真总线交互的目标设备或外设 |

## 476.2\_定义设备树仿真器

本节的宏均来自 `zephyr/drivers/emul.h`。[`EMUL_DT_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8) 向由**链接器（Linker）**收集的仿真器列表加入一个新的 `struct emul`，通常在仿真器的 [`DT_INST_FOREACH_STATUS_OKAY()`](../dt_instance_reference/P001_设备树驱动实例宏.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7) 展开中使用；这个设备树辅助宏遍历状态为 `okay` 的匹配实例。

```c
#define EMUL_DT_DEFINE(node_id, init_fn, data_ptr, cfg_ptr, bus_api, _backend_api)
```

| 参数 | 含义与要求 |
| --- | --- |
| `node_id` | 被仿真驱动的节点标识，例如 `DT_DRV_INST(n)`；该节点**必须**具有对应的 [`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 设备定义 |
| `init_fn` | 初始化仿真器的函数，见后文 [`emul_init_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaa6129de6e0edef345242559a3dac3a50) 回调类型 |
| `data_ptr` | 仿真器专用的数据 |
| `cfg_ptr` | 仿真器专用的配置数据 |
| `bus_api` | 仿真器专用的总线 API |
| `_backend_api` | 仿真器专用的后端 API |

展开中还使用 `EMUL_DT_NAME_GET` 宏构造唯一名称；`EMUL_BUS_TYPE_I2C`、`EMUL_BUS_TYPE_ESPI`、`EMUL_BUS_TYPE_SPI`、`EMUL_BUS_TYPE_MSPI`、`EMUL_BUS_TYPE_UART` 是各总线类型的枚举成员，`EMUL_BUS_TYPE_NONE` 表示无总线。

下面保留官方宏展开。其中 `Z_EMUL_BUS` 和 `Z_EMUL_REG_BUS_IDENTIFIER` 是内部辅助宏，分别用于按总线类型选取内容和构造注册标识；[`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 取得节点的设备对象，[`DT_REG_ADDR`](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e) 读取地址，[`STRUCT_SECTION_ITERABLE`](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f) 将对象放入可遍历的链接段，`__used` 标记对象应予保留。`IF_ENABLED` 与 [`DT_NODE_HAS_PROP`](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692) 控制属性存在时的条件展开。这些名称均是代码标识符。

```c
static struct Z_EMUL_BUS(node_id, i2c_emul, espi_emul, spi_emul, mspi_emul, uart_emul,     \
                         no_bus_emul) Z_EMUL_REG_BUS_IDENTIFIER(node_id) = {               \
        .api = bus_api,                                                                    \
        IF_ENABLED(DT_NODE_HAS_PROP(node_id, reg),                                         \
                   (.Z_EMUL_BUS(node_id, addr, chipsel, chipsel, dev_idx, dummy, addr) =   \
                            DT_REG_ADDR(node_id),))};                                      \
const STRUCT_SECTION_ITERABLE(emul, EMUL_DT_NAME_GET(node_id)) __used = {                  \
        .init = (init_fn),                                                                 \
        .dev = DEVICE_DT_GET(node_id),                                                     \
        .cfg = (cfg_ptr),                                                                  \
        .data = (data_ptr),                                                                \
        .bus_type = Z_EMUL_BUS(node_id, EMUL_BUS_TYPE_I2C, EMUL_BUS_TYPE_ESPI,             \
                               EMUL_BUS_TYPE_SPI, EMUL_BUS_TYPE_MSPI, EMUL_BUS_TYPE_UART,  \
                               EMUL_BUS_TYPE_NONE),                                        \
        .bus = {.Z_EMUL_BUS(node_id, i2c, espi, spi, mspi, uart, none) =                   \
                        &(Z_EMUL_REG_BUS_IDENTIFIER(node_id))},                            \
        .backend_api = (_backend_api),                                                     \
};
```

## 476.3\_取得实例与构造唯一名称

[`EMUL_DT_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga300d997df388118ae380e79b972f85cf) 根据设备树节点标识取得 `const struct emul *`。如果仿真器实现为节点分配了对象，返回指向该对象的指针。

```c
#define EMUL_DT_GET(node_id)
```

```c
(&EMUL_DT_NAME_GET(node_id))
```

如果没有分配对应设备，则会在链接阶段失败。例如出现 `undefined reference to __device_dts_ord_<N>` 一类错误时，应检查仿真器实现是否参与编译，通常需要启用它所依赖的 **Kconfig 配置选项（Kconfig Configuration Options）**。参数 `node_id` 是设备树节点标识，返回值是该节点的仿真器对象指针。

[`EMUL_DT_GET_OR_NULL`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gab37b4f8b4c434ca38f523eb6391d4e3b) 用于取得可选的仿真器引用：节点状态为 `okay` 时返回 `EMUL_DT_GET(node_id)`，否则返回空指针 `NULL`。参数仍为设备树节点标识，结果允许为 `NULL`。

```c
#define EMUL_DT_GET_OR_NULL(node_id)
```

展开中的 [`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 根据条件是否为 1 选择分支；[`DT_NODE_HAS_STATUS_OKAY`](../dt_identity_reference/P002_设备树存在性与状态宏.md#gaed773a8782fe00db90e8599ff673e8ed) 检查节点状态。

```c
COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(node_id), (EMUL_DT_GET(node_id)), (NULL))
```

> 译注：这里的“可选”是对节点状态而言。若状态为 `okay` 却没有编译出对应仿真对象，仍会走到 [`EMUL_DT_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga300d997df388118ae380e79b972f85cf)，不能把它当作忽略链接错误的运行时查询。

[`EMUL_DT_INST_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gafe7f4912bcffed1366ce07d024a4f977) 与 [`EMUL_DT_DEFINE()`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8) 相同，但通过 `DT_DRV_COMPAT` 指定的兼容字符串匹配实例，而不是直接传入节点标识。参数 `inst` 为实例编号，转换后的 `node_id` 为 `DT_DRV_INST(inst)`；其余可变参数原样传给 [`EMUL_DT_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8)。`__VA_ARGS__` 是 C 预处理器的可变参数占位符。

```c
#define EMUL_DT_INST_DEFINE(inst, ...)
```

```c
EMUL_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

[`EMUL_DT_NAME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gac1638c8cad48dab50f9ebc83592236db) 使用设备树节点标识构造唯一名称，参数 `node_id` 为节点标识。内部的 `_CONCAT` 执行标记拼接。

```c
#define EMUL_DT_NAME_GET(node_id)
```

```c
_CONCAT(__emulreg_, node_id)
```

## 476.4\_初始化回调与总线类型

`emul_init_t` 是仿真器初始化使用的标准**回调（Callback）**类型：框架向它提供初始化记录，以及调用仿真器函数的设备。

```c
typedef int (*emul_init_t)(const struct emul *emul,
                           const struct device *parent);
```

[`emul`](P477_仿真器实例结构.md) 指向待初始化的仿真器；`parent` 指向使用该仿真器的父设备。原页未单独规定该回调返回值的取值约定。

[`emul_bus_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga39b7a9438507b0be95038fe9464762aa) 枚举支持的总线类型，枚举声明和成员顺序如下：

```c
enum emul_bus_type {
    EMUL_BUS_TYPE_I2C,
    EMUL_BUS_TYPE_ESPI,
    EMUL_BUS_TYPE_SPI,
    EMUL_BUS_TYPE_MSPI,
    EMUL_BUS_TYPE_UART,
    EMUL_BUS_TYPE_NONE
};
```

前五项依次表示 I2C、eSPI、SPI、MSPI、UART 总线；[`EMUL_BUS_TYPE_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d) 表示仿真器没有附着在总线上。各总线名称的中英文对照见本章子主题表。

## 476.5\_按名称查询与初始化总线列表

[`emul_get_binding()`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaad94c1e07998417cb9aa06d03be3b280) 按名称取得仿真器的 [`emul`](P477_仿真器实例结构.md) 结构。对象由 [`EMUL_DT_DEFINE()`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8) 创建，再由链接器放入内存。调用自定义 API 需要该结构时，可以用仿真器向系统暴露的名称查询；原文说明，默认名称是设备树节点的标签（Label）。

```c
const struct emul *emul_get_binding(const char *name);
```

参数 `name` 为待查找的仿真器名称。传入空指针或指向空字符串的指针都会返回 `NULL`。找到且可用时返回仿真器结构指针；找不到或无法使用时返回 `NULL`。

[`emul_init_for_bus()`](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad587b2852a182e1a7fdcb3b056d898f1) 建立一组仿真器的列表：参数 `dev` 是这些仿真器所附着的设备，例如一个 I2C 控制器（Controller）。

```c
int emul_init_for_bus(const struct device *dev);
```

成功返回 `0`；发生错误返回负值。这两个函数也由 `zephyr/drivers/emul.h` 声明。

---

[上一章：外部总线与外设仿真](P475_外部总线与外设仿真.md) · [下一章：仿真器实例结构](P477_仿真器实例结构.md) · [返回大纲](大纲.md)
