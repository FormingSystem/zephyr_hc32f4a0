---
id: learning.zephyr-docs.hardware.gpiodt-0
title: 设备树GPIO宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第290章\_设备树GPIO宏

原文：[group__devicetree-gpio](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html)。读取日期：2026-10-13，`latest`。

## 290.1\_公共参数与描述符

本页提供设备树（Devicetree）的通用输入/输出（General Purpose Input/Output，GPIO）访问宏，声明来自 `zephyr/devicetree/gpio.h`。相关子分组为[GPIO排针](P291_GPIO排针目录.md)，定义常见排针对外引脚的常量。

GPIO描述符（GPIO Specifier）由控制器节点句柄（Phandle）及引脚、标志等参数单元（Cell）组成；绑定（Binding）规定各单元的名字。

| 参数 | 含义 |
| --- | --- |
| `node_id` | 节点标识符（Node Identifier） |
| `gpio_pha` | 类型为节点句柄数组（Phandle Array，`phandle-array`）的GPIO属性名，用小写字母及下划线书写 |
| `idx` | 属性中的逻辑索引，从零开始；GPIO独占配置宏中指 `gpios` 属性索引 |
| `inst` | 与驱动兼容标识 `DT_DRV_COMPAT` 匹配的实例编号 |

下文示例中 `GPIO_ACTIVE_LOW` 为低电平有效（Active Low），`GPIO_ACTIVE_HIGH` 为高电平有效（Active High）；`DT_NODELABEL()` 根据节点标签取得节点标识符。GPIO独占配置（GPIO Hog）使用带 `gpio-hog` 属性的节点描述自动占用配置的引脚。

## 290.2\_控制器节点

<a id="gafbad7d0d7f7fb9338997482c8da0e566"></a>

宏 `DT_GPIO_CTLR(node_id, gpio_pha)` 返回属性索引0引用的GPIO控制器节点标识符，等价于指定索引0的调用：

```c
DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, 0)
```

<a id="ga97bd46d2ab88d392a3f336f4d23184eb"></a>

宏 `DT_GPIO_CTLR_BY_IDX(node_id, gpio_pha, idx)` 返回属性索引 `idx` 所引用的控制器节点标识符，使用节点句柄读取宏 [`DT_PHANDLE_BY_IDX()`](../dt_property_reference/P001_设备树属性读取宏.md#ga8ff163c240878a988d29d727671671de)：

```c
DT_PHANDLE_BY_IDX(node_id, gpio_pha, idx)
```

原设备树片段：

```dts
gpio1: gpio@... { };

gpio2: gpio@... { };

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

原用法和返回的节点标识符：

```c
DT_GPIO_CTLR_BY_IDX(DT_NODELABEL(n), gpios, 1) // DT_NODELABEL(gpio2)
```

## 290.3\_GPIO标志

<a id="ga32b3383d7ed543602a7b4a031018316f"></a>

宏 `DT_GPIO_FLAGS(node_id, gpio_pha)` 返回索引0的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值；没有该单元时返回0：

```c
DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, 0)
```

<a id="ga672b2597b99194b8cbd42b3f3401d2b5"></a>

宏 `DT_GPIO_FLAGS_BY_IDX(node_id, gpio_pha, idx)` 返回索引 `idx` 的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值；没有该单元时返回0。它预期描述符有名为 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 的单元，必要时应检查节点绑定。原展开使用带缺省值的参数单元读取宏 [`DT_PHA_BY_IDX_OR()`](../dt_property_reference/P001_设备树属性读取宏.md#gad830ed96dbc4f7dac3455153e0a944d6)，相关宏为 [`DT_PHA_BY_IDX()`](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)：

```c
DT_PHA_BY_IDX_OR(node_id, gpio_pha, idx, flags, 0)
```

原设备树片段：

```dts
gpio1: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

gpio2: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

兼容属性为 `vnd,gpio` 的绑定片段：

```yaml
gpio-cells:
  - pin
  - flags
```

原用法：

```c
DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 0) // GPIO_ACTIVE_LOW
DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 1) // GPIO_ACTIVE_HIGH
```

## 290.4\_GPIO独占配置标志

<a id="gaed024e6acac49f591fe50cd43e8af14f"></a>

宏 `DT_GPIO_HOG_FLAGS_BY_IDX(node_id, idx)` 返回独占配置节点索引 `idx` 的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 单元值；没有该单元时返回0。需要时检查绑定中的单元名称。

原展开中，[`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 选择条件分支，[`IS_ENABLED`](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a) 检查生成标识，`DT_CAT4` 拼接四段标识：

```c
COND_CODE_1(IS_ENABLED(DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_flags_EXISTS)), \
            (DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_flags)), (0))
```

原设备树片段中，`output-high`、`output-low` 分别表示高、低输出配置：

```dts
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

对应 `vnd,gpio` 绑定片段：

```yaml
gpio-cells:
  - pin
  - flags
```

原用法：

```c
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 0) // GPIO_ACTIVE_HIGH
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 1) // GPIO_ACTIVE_LOW
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n2), 0) // GPIO_ACTIVE_HIGH
```

## 290.5\_GPIO独占配置引脚

<a id="gaf4ecdebbd433473f654f4b6859542af9"></a>

宏 `DT_GPIO_HOG_PIN_BY_IDX(node_id, idx)` 返回独占配置节点索引 `idx` 的 `pin` 单元值。它仅适用于具有名为 `pin` 的参数单元的描述符；必要时检查绑定。

```c
DT_CAT4(node_id, _GPIO_HOGS_IDX_, idx, _VAL_pin)
```

原设备树片段：

```dts
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

对应 `vnd,gpio` 绑定：

```yaml
gpio-cells:
  - pin
  - flags
```

原调用及引脚编号：

```c
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 0) // 0
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 1) // 1
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n2), 0) // 3
```

## 290.6\_普通GPIO引脚

<a id="ga4e41ec30ece058555333811a9fcee333"></a>

宏 `DT_GPIO_PIN(node_id, gpio_pha)` 返回索引0的 `pin` 参数单元值：

```c
DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, 0)
```

<a id="ga8f7d82567056266bab1603865f8b27af"></a>

宏 `DT_GPIO_PIN_BY_IDX(node_id, gpio_pha, idx)` 返回指定索引的 `pin` 单元值，且仅适用于单元名为 `pin` 的描述符；必要时检查绑定。它基于 [`DT_PHA_BY_IDX()`](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)：

```c
DT_PHA_BY_IDX(node_id, gpio_pha, idx, pin)
```

原设备树片段：

```dts
gpio1: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

gpio2: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

对应 `vnd,gpio` 绑定：

```yaml
gpio-cells:
  - pin
  - flags
```

原用法：

```c
DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 0) // 10
DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 1) // 30
```

## 290.7\_实例的GPIO标志与引脚

以下宏由 `DT_DRV_INST(inst)` 取得对应实例节点，再应用节点版规则。

<a id="ga8d3edd53d6d8e89afc68f0c10176f57f"></a>

宏 `DT_INST_GPIO_FLAGS(inst, gpio_pha)` 返回实例属性索引0的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 单元值；没有该单元时返回0：

```c
DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, 0)
```

<a id="gafd40d1eec5c1672b7675ae47388c1cef"></a>

宏 `DT_INST_GPIO_FLAGS_BY_IDX(inst, gpio_pha, idx)` 返回实例属性指定索引的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 单元值；没有该单元时返回0：

```c
DT_GPIO_FLAGS_BY_IDX(DT_DRV_INST(inst), gpio_pha, idx)
```

<a id="ga5ee13b3de1d4cecc877963dfa8820cfd"></a>

宏 `DT_INST_GPIO_PIN(inst, gpio_pha)` 返回实例属性索引0的 `pin` 单元值：

```c
DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, 0)
```

<a id="ga162bca126f7015816286358f09bde6ff"></a>

宏 `DT_INST_GPIO_PIN_BY_IDX(inst, gpio_pha, idx)` 返回实例属性指定索引的 `pin` 单元值：

```c
DT_GPIO_PIN_BY_IDX(DT_DRV_INST(inst), gpio_pha, idx)
```

## 290.8\_独占配置引脚数量

<a id="ga0a4575c3750db76692fd0f817a169b50"></a>

宏 `DT_NUM_GPIO_HOGS(node_id)` 展开为节点中独占配置的GPIO数量，没有则为0。参数 `node_id` 可以是GPIO独占配置节点，也可以不是。原展开使用标识拼接宏 `DT_CAT()`：

```c
COND_CODE_1(IS_ENABLED(DT_CAT(node_id, _GPIO_HOGS_EXISTS)), \
            (DT_CAT(node_id, _GPIO_HOGS_NUM)), (0))
```

原设备树片段：

```dts
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

对应 `vnd,gpio` 绑定：

```yaml
gpio-cells:
  - pin
  - flags
```

原调用分别得到2和1：

```c
DT_NUM_GPIO_HOGS(DT_NODELABEL(n1)) // 2
DT_NUM_GPIO_HOGS(DT_NODELABEL(n2)) // 1
```

---

[上一章：BL61x线输出配置](P289_BL61x线输出配置.md) · [下一章：GPIO排针目录](P291_GPIO排针目录.md) · [返回大纲](大纲.md)
