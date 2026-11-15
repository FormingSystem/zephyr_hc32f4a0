---
id: learning.zephyr-docs.kconfig.kconfig-preprocessor
title: Kconfig预处理函数
kind: reference
status: maintained
domains: [zephyr, kconfig]
source_url: https://docs.zephyrproject.org/latest/build/kconfig/preprocessor-functions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_Kconfig预处理函数

原文：[Custom Kconfig Preprocessor Functions](https://docs.zephyrproject.org/latest/build/kconfig/preprocessor-functions.html)。读取日期：2026-10-12，`latest`。

Kconfiglib 支持用 Python 编写自定义 **Kconfig预处理函数（Kconfig Preprocessor Function）**。它们定义在 [`scripts/kconfig/kconfigfunctions.py`](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfigfunctions.py)，详细行为见各函数的 Python 文档字符串。

大多数函数把**设备树（Devicetree）**信息带入 Kconfig，例如从节点 `reg` 属性取得某个配置符号的默认值。通用预处理语法见 [Kconfig预处理器文档](https://www.kernel.org/doc/html/latest/kbuild/kconfig-macro-language.html)。

## 6.1\_设备树相关函数

下列完整列表保留函数名与参数位置。`*_int` 版本返回十进制整数形式，`*_hex` 版本返回带 `0x` 前缀的十六进制形式。

> 译注：签名中的尖括号是参数占位，方括号表示可选参数。`node alias` 是节点别名，`node label` 是节点标签，`node path` 是设备树节点路径；`property in /chosen` 是选择节点内的属性名。`prop` 指属性，`index` 指元素索引，`cell` 指说明符单元名，`unit` 是函数支持的可选单位，`compatible string` 指硬件匹配字符串，`bus` 是总线类型，`class name` 是设备类名。这些是 Kconfig 文件内的调用形式，不是 Shell 命令；实际可选单位和缺失节点行为应按所用版本的函数文档核对。

```kconfig
$(dt_alias_enabled,<node alias>)
$(dt_chosen_bool_prop, <property in /chosen>, <prop>)
$(dt_chosen_enabled,<property in /chosen>)
$(dt_chosen_has_compat,<property in /chosen>,<compatible string>)
$(dt_chosen_label,<property in /chosen>)
$(dt_chosen_partition,addr_hex,<chosen>[,<index>,<unit>])
$(dt_chosen_partition,addr_int,<chosen>[,<index>,<unit>])
$(dt_chosen_path,<property in /chosen>)
$(dt_chosen_reg_addr_hex,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_addr_int,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_size_hex,<property in /chosen>[,<index>,<unit>])
$(dt_chosen_reg_size_int,<property in /chosen>[,<index>,<unit>])
$(dt_class_enabled,<class name>)
$(dt_compat_all_has_prop,<compatible string>,<prop>[,<value>])
$(dt_compat_any_has_prop,<compatible string>,<prop>[,<value>])
$(dt_compat_any_on_bus,<compatible string>,<prop>)
$(dt_compat_enabled,<compatible string>)
$(dt_compat_enabled_num,<compatible string>)
$(dt_compat_on_bus,<compatible string>,<bus>)
$(dt_gpio_hogs_enabled)
$(dt_has_compat,<compatible string>)
$(dt_highest_controller_irq_number,<node path>,<cell>)
$(dt_node_array_prop_has_val,<node path>,<prop>,<value>)
$(dt_node_array_prop_hex,<node path>,<prop>,<index>[,<unit>])
$(dt_node_array_prop_int,<node path>,<prop>,<index>[,<unit>])
$(dt_node_bool_prop,<node path>,<prop>)
$(dt_node_has_compat,<node path>,<compatible string>)
$(dt_node_has_prop,<node path>,<prop>)
$(dt_node_int_prop_hex,<node path>,<prop>[,<unit>])
$(dt_node_int_prop_int,<node path>,<prop>[,<unit>])
$(dt_node_parent,<node path>)
$(dt_node_ph_array_prop_hex,<node path>,<prop>,<index>,<cell>[,<unit>])
$(dt_node_ph_array_prop_int,<node path>,<prop>,<index>,<cell>[,<unit>])
$(dt_node_ph_prop_path,<node path>,<prop>)
$(dt_node_reg_addr_hex,<node path>[,<index>,<unit>])
$(dt_node_reg_addr_int,<node path>[,<index>,<unit>])
$(dt_node_reg_size_hex,<node path>[,<index>,<unit>])
$(dt_node_reg_size_int,<node path>[,<index>,<unit>])
$(dt_node_str_prop_equals,<node path>,<prop>,<value>)
$(dt_nodelabel_array_prop_has_val, <node label>, <prop>, <value>)
$(dt_nodelabel_bool_prop,<node label>,<prop>)
$(dt_nodelabel_enabled,<node label>)
$(dt_nodelabel_enabled_with_compat,<node label>,<compatible string>)
$(dt_nodelabel_exists,<node label>)
$(dt_nodelabel_has_compat,<node label>,<compatible string>)
$(dt_nodelabel_has_prop,<node label>,<prop>)
$(dt_nodelabel_path,<node label>)
$(dt_nodelabel_reg_addr_hex,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_addr_int,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_size_hex,<node label>[,<index>,<unit>])
$(dt_nodelabel_reg_size_int,<node label>[,<index>,<unit>])
$(dt_path_enabled,<node path>)
$(dt_partition_mtd,<node path>)
```

> 译注：函数名中的 `chosen`、`nodelabel`、`node`、`compat` 区分查找入口；`enabled`、`exists`、`has_prop` 等表示不同检查，不能因名称相近就互换。原清单还包含 `dt_compat_any_on_bus`，但当前仓库函数注册表未提供这个名称；可查到的 `dt_compat_on_bus` 接收匹配字符串和总线名。原列表保留以供版本对照，不能直接假定额外的 `any` 名称在本地也可调用，或自行把两个名称当作别名。

## 6.2\_整数运算函数

以下函数对整数执行加、减等运算。名称带 `_hex` 时返回十六进制形式，不带时返回十进制形式：

```kconfig
$(add,<value>[,value]...)
$(add_hex,<value>[,value]...)
$(dec,<value>[,value]...)
$(dec_hex,<value>[,value]...)
$(div,<value>[,value]...)
$(div_hex,<value>[,value]...)
$(inc,<value>[,value]...)
$(inc_hex,<value>[,value]...)
$(max,<value>[,value]...)
$(max_hex,<value>[,value]...)
$(min,<value>[,value]...)
$(min_hex,<value>[,value]...)
$(mod,<value>[,value]...)
$(mod_hex,<value>[,value]...)
$(mul,<value>[,value]...)
$(mul_hex,<value>[,value]...)
$(sub,<value>[,value]...)
$(sub_hex,<value>[,value]...)
```

> 译注：`add/sub/mul/div/mod` 分别用于加、减、乘、除及取余，`max/min` 取最大/最小值，`inc/dec` 为增一/减一。仓库函数文档说明 `inc/dec` 对序列中每项操作并返回逗号分隔结果；不能把多个参数理解成最终只返回一个加总值。具体运算顺序和除法边界以版本实现为准，本页没有执行运算测试。

## 6.3\_字符串处理函数

字符串函数的调用形式为：

```kconfig
$(normalize_upper,<string>)
$(substring,<string>,<start>[,<stop>])
```

> 译注：`normalize_upper` 规范化字符串，将非字母数字或下划线的字符替换成下划线，再转为大写。`substring` 按起始位置 `start` 与可选终止位置 `stop` 取得子串；仓库实现使用 Python 切片，终止位置不包含在结果中，未给出时取到末尾。

## 6.4\_检查扩展板选择

原文“其他函数”目前列出检查**扩展板（Shield）**名称是否在选择列表中的函数：

```kconfig
$(shields_list_contains,<shield name>)
```

扩展板名称不能包含空白。根据所读取原文，若像 `$(shields_list_contains, foo)` 一样在逗号后加空格，会去掉空格并打印警告，因此仍能匹配 `foo`。

> 译注：这是 `latest` 文档描述的行为；当前仓库中的函数版本直接比较分号分隔列表，未在该函数内看到去空白和警告逻辑。不同源码版本应分别核对，编写配置时应直接使用不带多余空格的名称，不依赖容错行为。

## 6.5\_从reg属性取得默认地址

假设某板的设备树片段为：

```dts
{
     soc {
             #address-cells = <1>;
             #size-cells = <1>;

             spi0: spi@10014000 {
                     compatible = "sifive,spi0";
                     reg = <0x10014000 0x1000 0x20010000 0x3c0900>;
                     reg-names = "control", "mem";
                     ...
             };
};
```

`#address-cells` 与 `#size-cells` 都为 1，因此 `reg` 中每个区域由一个地址单元加一个大小单元组成。第二个区域 `<0x20010000 0x3c0900>` 对应 `reg-names` 中的 `mem`，其地址是 `0x20010000`。

原文用下面的 Kconfig 片段获取第二个区域，即索引 1：

```kconfig
config FLASH_BASE_ADDRESS
     default $(dt_node_reg_addr_hex,/soc/spi@1001400,1)
```

展开后的预期定义为：

```kconfig
config FLASH_BASE_ADDRESS
     default 0x20010000
```

> 译注：原文示例有两处不完整或不一致：设备树片段省略了根节点 `/` 和完整闭合结构，不能作为完整**设备树源文件（Devicetree Source，DTS）**直接使用；函数调用写成 `/soc/spi@1001400`，比上方节点 `spi@10014000` 少一个 `0`。若按上方节点访问，应写 `$(dt_node_reg_addr_hex,/soc/spi@10014000,1)`，才能与所示地址对应。这里的斜线路径属于设备树内部，不是主机绝对文件地址。原代码保留以供对照，不能把展示的期望展开值当成实际执行结果。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Kconfig扩展](P005_Kconfig扩展.md) · [本模块主线目录](../reading/kconfig.md) · [全部主线](../reading/README.md) · [下一篇：追踪配置值来源](P007_追踪配置值来源.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Kconfig扩展](P005_Kconfig扩展.md) · [返回大纲](大纲.md) · [下一章：追踪配置值来源](P007_追踪配置值来源.md)

</details>

<!-- reading-navigation:end -->
