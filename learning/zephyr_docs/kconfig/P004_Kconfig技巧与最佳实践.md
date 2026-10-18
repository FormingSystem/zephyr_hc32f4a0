---
id: learning.zephyr-docs.kconfig.tips
title: Kconfig技巧与最佳实践
kind: reference
status: maintained
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/build/kconfig/tips.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="kconfig-tips-and-tricks"></a>

# 第4章\_Kconfig技巧与最佳实践

原文：[Kconfig - Tips and Best Practices](https://docs.zephyrproject.org/latest/build/kconfig/tips.html)。读取日期：2026-10-12，`latest`。

本页介绍 Kconfig 最佳实践，并解释一些难理解或容易忽略的行为。Kconfig 语言的官方参考为 [kconfig-language.rst](https://www.kernel.org/doc/html/latest/kbuild/kconfig-language.html) 和 [kconfig-macro-language.rst](https://www.kernel.org/doc/html/latest/kbuild/kconfig-macro-language.html)。

## 4.1\_哪些内容适合做成配置项

决定某项设置是否属于 Kconfig 时，应先区分符号是否有提示（prompt）。例如 `bool "Enable foo"` 有提示，用户可以在 menuconfig、guiconfig 或配置文件中修改它。没有提示的符号不能由用户直接配置，即使手动编辑配置文件也不行。

只有允许用户修改其值确实有意义时，才应给符号添加提示。无提示符号称为隐藏或不可见符号，不出现在交互界面；有提示的符号在依赖不满足时也可能不可见。

无提示符号从其他符号推导取值，因此约束较少。如果某个派生值用 Kconfig 比在构建脚本中更容易计算，就可以放在 Kconfig 中，但不要混淆它与用户可配置选项。

某些机器固定、另一些机器可配置的值，可以通过后文的“可选提示”表达。

## 4.2\_哪些内容不应做成配置项

Zephyr 在选定开发板后才运行 Kconfig。固定的机器专用硬件设置通常不应由 Kconfig 表达，而应放在设备树中，尤其应避免以下两类新选项。

### 4.2.1\_按名称指定设备

例如 **集成电路间总线（Inter-Integrated Circuit，I2C）** 设备驱动不应增加 `MY_DEVICE_I2C_BUS_NAME` 来指定控制该设备的总线节点；替代方案见[依赖其他设备的驱动](../devicetree/P006_设备树操作指南.md)。应用为了用 **脉宽调制（Pulse Width Modulation，PWM）** 控制 RGB **发光二极管（Light-Emitting Diode，LED）**，也不应增加 `MY_PWM_DEVICE_NAME`；应采用该指南中按板级设备描述取得设备的方法。

### 4.2.2\_固定硬件配置

例如 **通用输入输出（General-Purpose Input/Output，GPIO）** 引脚号不适合做成 Kconfig。驱动可在绑定中定义 `phandle-array` 类型的 GPIO 指示符属性，再从 C 使用设备树 GPIO **应用程序编程接口（Application Programming Interface，API）**。`devicetree.h` 提供的其他硬件专用引用 API 也适用同一原则，可在已有驱动中查找例子。

应用还可以使用自定义绑定标识板专用属性，参考 [tests/drivers/gpio/gpio_basic_api](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/drivers/gpio/gpio_basic_api)。基本应用示例见[LED 闪烁译文](../getting_started/P004_LED闪烁示例.md)。

## 4.3\_select及其风险

`select` 会在一个符号为 `y` 时，强制另一个符号为 `y`。以下代码使 `USB_CONSOLE=y` 时 `CONSOLE` 也为 `y`：

```kconfig
config CONSOLE
     bool "Console support"

...

config USB_CONSOLE
     bool "USB console support"
     select CONSOLE
```

看似方便，但过度使用容易破坏配置依赖。假设某位开发者不知道或忘记 `USB_CONSOLE` 的存在，给 `CONSOLE` 增加依赖：

```kconfig
config CONSOLE
     bool "Console support"
     depends on STRING_ROUTINES
```

此时，即使 `STRING_ROUTINES=n`，启用 **通用串行总线（Universal Serial Bus，USB）** 控制台仍会强制 `CONSOLE=y`，绕过其依赖。要修复，就必须给选择它的符号也加同一依赖：

```kconfig
config USB_CONSOLE
     bool "USB console support"
     select CONSOLE
     depends on STRING_ROUTINES

...

config STRING_ROUTINES
     bool "Include string routines"
```

如果依赖从 `if` 或 `menu` 继承，问题更隐蔽。另一个看似可行的方案是继续使用 `select`：

```kconfig
config CONSOLE
     bool "Console support"
     select STRING_ROUTINES

...

config USB_CONSOLE
     bool "USB console support"
     select CONSOLE
```

这样通常会放大问题：以后 `STRING_ROUTINES` 新增依赖时，又必须同时复制到 `CONSOLE` 和 `USB_CONSOLE`。

一般而言，被选符号的依赖发生变化时，所有直接或间接 `select` 它的符号都需要同步更新。实践中非常容易遗漏，所以应避免形成选择链，简单辅助符号除外。

大量 `select` 也会降低可读性：除了额外依赖，它还让“谁能启用这个符号”分散到其他位置，很难就地理解。

## 4.4\_用depends on代替强制选择

前例通常更适合改成依赖：

```kconfig
config CONSOLE
     bool "Console support"

...

config USB_CONSOLE
     bool "USB console support"
     depends on CONSOLE
```

这样不会产生违反依赖的配置，依赖也只需在一处维护。代价是启用 USB 控制台的配置文件需要同时打开控制台：

```ini
CONFIG_CONSOLE=y
CONFIG_USB_CONSOLE=y
```

这是可维护性与配置长度之间的取舍。如果大多数场景本来就需要控制台，可以给它默认值 `y`：

```kconfig
config CONSOLE
     bool "Console support"
     default y
```

此时常见配置只需写：

```ini
CONFIG_USB_CONSOLE=y
```

但不需要控制台的配置就必须显式关闭：

```ini
CONFIG_CONSOLE=n
```

## 4.5\_辅助符号与select使用建议

`select` 的安全用途之一是设置用于表达某项条件的辅助符号。辅助符号最好没有提示，也没有依赖。

例如，用 `CPU_HAS_FPU` 表示 **中央处理器（Central Processing Unit，CPU）**/**片上系统（System on Chip，SoC）** 是否有浮点单元：

```kconfig
config CPU_HAS_FPU
     bool
     help
       If y, the CPU has an FPU

...

config SOC_FOO
    bool
    select CPU_HAS_FPU

...

config SOC_BAR
    bool
    select CPU_HAS_FPU
```

其他选项就可以统一判断硬件能力：

```kconfig
config FPU
     bool "Support floating point operations"
     depends on CPU_HAS_FPU
```

否则可能需要在多处重复列出具体 SoC：

```kconfig
config FPU
     bool "Support floating point operations"
     depends on SOC_FOO || SOC_BAR || ...
```

隐藏辅助符号也可以不使用 `select`。例如按内存大小推导“内存较大”这一条件：

```kconfig
config LARGE_MEM
     def_bool MEM_SIZE >= 64
```

它是下面写法的缩写：

```kconfig
config LARGE_MEM
  bool
  default MEM_SIZE >= 64
```

原文对 `select` 的建议如下：

- 避免选择有提示或有依赖的符号，优先 `depends on`。如果配置文件因此过长，可考虑给常见取值增加默认值。
- 极少数例外是能够确定两边依赖不会不同步的简单场景，例如同一 `if` 内相邻定义的两个简单符号。仍应意识到 `select` 在实践中经常引发问题。
- 无提示、无依赖的简单辅助符号适合被 `select`，可以放心用来简化结构。
- I2C、**串行外设接口（Serial Peripheral Interface，SPI）** 等总线，以及按类似原则处理的多功能设备 MFD，是一个例外：总线上的设备驱动应选择所需总线，使设备树中启用设备时可自动激活必要总线驱动。例如：

```kconfig
config ADC_FOO
   bool "external SPI ADC foo driver"
   select SPI
```

## 4.6\_if不会有条件地包含文件

`if` 为块内所有条目添加依赖，效果类似各条目分别写 `depends on`。下面并不表示只有 `DEP` 成立才读取文件：

```kconfig
if DEP

source "Kconfig.other"

endif
```

Kconfig 没有这种条件包含机制，`source` 外的 `if` 没有特殊含义。原因之一是 `if` 条件可能直接或间接引用尚未定义的符号，不能依靠当前值决定是否读取后续定义。

假设 `Kconfig.other` 中有：

```kconfig
config FOO
     bool "Support foo"
```

最终等价于：

```kconfig
config FOO
     bool "Support foo"
     depends on DEP
```

因此无需在被包含文件中再次添加 `depends on DEP`。应尽量避免冗余依赖，否则结构更难理解，修改时也不容易发现同一约束已出现两遍。

## 4.7\_为什么界面中的值似乎被固定住

相互依赖、同时又有提示的符号存在一个常见陷阱。考虑：

```kconfig
config FOO
     bool "Foo"

config STACK_SIZE
     hex "Stack size"
     default 0x200 if FOO
     default 0x100
```

意图是启用 `FOO` 时使用更大的栈。假设最初 `FOO` 关闭，Zephyr 在运行 menuconfig 或 guiconfig 前，已经把 `prj.conf` 等片段合并到构建目录的 `zephyr/.config`。

首次进入界面，`STACK_SIZE=0x100` 符合预期；启用 `FOO` 后，它却不变成 `0x200`。原因是已有配置中写着：

```ini
CONFIG_STACK_SIZE=0x100
```

Kconfig 无法知道这个值来自默认值还是用户亲自输入；因为 `STACK_SIZE` 有提示、允许用户设置，它必须尊重配置文件中的值，忽略新的默认值。这就造成“固定住”的现象。

修复方式取决于真实意图。

### 4.7.1\_始终自动推导

如果完全不需要用户修改，移除提示：

```kconfig
config STACK_SIZE
   hex
   default 0x200 if FOO
   default 0x100
```

无提示符号会忽略已保存配置中的赋值。

### 4.7.2\_仅在特定条件下固定

若平时允许配置，但启用 `FOO` 时必须为 `0x200`，则在该条件下隐藏提示：

```kconfig
config STACK_SIZE
   hex "Stack size" if !FOO
   default 0x200 if FOO
   default 0x100
```

### 4.7.3\_只有明确选择自定义时才允许修改

若通常自动推导，只有少数场景需要自定义，可增加一个开关：

```kconfig
config CUSTOM_STACK_SIZE
   bool "Use a custom stack size"
   help
     Enable this if you need to use a custom stack size. When disabled, a
     suitable stack size is calculated automatically.

config STACK_SIZE
   hex "Stack size" if CUSTOM_STACK_SIZE
   default 0x200 if FOO
   default 0x100
```

只要 `CUSTOM_STACK_SIZE` 未启用，`STACK_SIZE` 就忽略已保存配置中的值。完成这类较复杂修改后，应在 menuconfig 或 guiconfig 中实际检查行为是否符合预期。

## 4.8\_隐藏符号赋值为何出现在.config

对无提示的隐藏符号，配置文件中的赋值始终被忽略；其值通过 `default`、`select` 等间接得到。

常见误解是：打开生成的 `zephyr/.config`，看到许多隐藏符号赋值，就认为再次读入时必须尊重它们。实际上，Kconfig 仍会忽略这些赋值。

原因在于 `.config` 有两个用途：保存配置，同时作为配置输出。例如 CMake 解析它以查询配置结果。隐藏符号赋值属于第二种用途，是计算后的输出，并非用户可直接设置的输入。

在交互界面生成的最小配置，更接近纯粹“保存配置”，不包含完整计算结果。

## 4.9\_非布尔符号也需要依赖

`depends on` 不只适用于 `bool`，也适用于 `string`、`int`、`hex` 和 choice。例如：

```kconfig
config FOO_DEVICE
     bool "Foo device"

config FOO_DEVICE_FREQUENCY
     int "Foo device frequency"
     depends on FOO_DEVICE
```

关闭 `FOO_DEVICE` 时，频率符号会隐藏，也不产生配置输出。界面应只显示当前相关符号；即使代码在设备关闭时不会读取频率，让该频率仍出现在界面也会使依赖关系难以理解。

## 4.10\_menuconfig符号

如果 `FOO` 后紧接一组依赖它的符号，这些符号会成为它的子项。使用 `config FOO` 时，子项缩进显示；改用 `menuconfig FOO` 时，子项放入以它为入口的单独菜单。

`menuconfig` 只改变显示，不改变求值规则，可以减少菜单层数。例如：

```kconfig
menu "Foo subsystem"

config FOO_SUBSYSTEM
     bool "Foo subsystem"

if FOO_SUBSYSTEM

config FOO_FEATURE_1
     bool "Foo feature 1"

config FOO_FEATURE_2
     bool "Foo feature 2"

config FOO_FREQUENCY
     int "Foo frequency"

... lots of other FOO-related symbols

endif # FOO_SUBSYSTEM

endmenu
```

通常可去掉外层 `menu`，改为：

```kconfig
menuconfig FOO_SUBSYSTEM
     bool "Foo subsystem"

if FOO_SUBSYSTEM

config FOO_FEATURE_1
     bool "Foo feature 1"

config FOO_FEATURE_2
     bool "Foo feature 2"

config FOO_FREQUENCY
     int "Foo frequency"

... lots of other FOO-related symbols

endif # FOO_SUBSYSTEM
```

交互界面显示：

```text
[*] Foo subsystem  --->
```

没有子项的符号不应写成 `menuconfig`，这没有意义，而且外观与“有子项但全部不可见”相同，容易误导：

```text
[*] I have no children  ----
[*] All my children are invisible  ----
```

两行英文分别表示“我没有子项”和“我的所有子项均不可见”。

## 4.11\_宏参数中的逗号

Kconfig 用逗号分隔宏参数，因此以下写法会失败：

```kconfig
config FOO
    bool
    default y if $(dt_chosen_enabled,"zephyr,bar")
```

解决方法是先把含逗号的文本存入变量，再传变量：

```kconfig
DT_CHOSEN_ZEPHYR_BAR := zephyr,bar

config FOO
    bool
    default y if $(dt_chosen_enabled,$(DT_CHOSEN_ZEPHYR_BAR))
```

对设备树绑定中出现的每个 compatible，Zephyr 已自动建立形如 `DT_COMPAT_VND_MY_DEVICE := vnd,my-device` 的变量，无须手动重复定义。参见[设备树与 Kconfig](../devicetree/P005_设备树与Kconfig.md)中的自动符号说明。

## 4.12\_在交互界面检查修改

新增或修改 Kconfig 后，建议在 menuconfig 或 guiconfig 中找到相关符号。按 `/` 可跳转。重点检查：

1. 符号是否位于合理菜单，是否靠近相关项。依赖另一符号的项通常放在它后面；menuconfig 会缩进显示，guiconfig 会放入以依赖符号为根的子菜单，多个连续子项也适用。
2. 提示文字是否让人容易猜到用途。
3. 所有可选组合是否有意义。例如同时允许 `FOO_SUPPORT`、`NO_FOO_SUPPORT` 为真会产生矛盾，通常只保留一个 `FOO_SUPPORT` 更好。
4. 是否重复添加依赖。选中符号按 `?` 查看信息，再通过 `Included via ...` 路径查找依赖来源。

界面操作详见[交互式配置界面](P002_交互式配置界面.md)。

### 4.12.1\_使用lint脚本

修改后可运行 [scripts/kconfig/lint.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/lint.py)，检查未使用符号、永远无法启用的符号等问题。用 `--help` 查看选项。

一些检查只能启发式判断，提示不一定是真问题。例如 C 中通过 `CONFIG_FOO_##index##_BAR` 拼接名字时可能误报，可以在核实后忽略。

调查未知符号 `FOO_BAR` 时，原文建议运行 `git grep FOO_BAR`；还应分别搜索 `git grep FOO`、`git grep BAR`，以发现 token 拼接。

## 4.13\_提取公共依赖

连续一组符号或 choice 共享同一依赖时，可用 `if` 提取。例如：

```kconfig
config FOO
     bool "Foo"
     depends on DEP

config BAR
     bool "Bar"
     depends on DEP

choice
     prompt "Choice"
     depends on DEP

config BAZ
     bool "Baz"

config QAZ
     bool "Qaz"

endchoice
```

可改为：

```kconfig
if DEP

config FOO
     bool "Foo"

config BAR
     bool "Bar"

choice
     prompt "Choice"

config BAZ
     bool "Baz"

config QAZ
     bool "Qaz"

endchoice

endif # DEP
```

内部处理时，第二种写法仍会转换成第一种等效依赖。如果这一组都在同一个菜单内，也可把依赖写在菜单上：

```kconfig
menu "Foo features"
     depends on FOO_SUPPORT

config FOO_FEATURE_1
     bool "Foo feature 1"

config FOO_FEATURE_2
     bool "Foo feature 2"

endmenu
```

`FOO_SUPPORT=n` 时整个菜单消失。

## 4.14\_省略冗余默认值

`bool` 隐式默认 `n`，`string` 隐式默认空字符串，因此 `default n`、`default ""` 几乎总是冗余。Zephyr 推荐省略它们，也能生成更清楚的文档：说明“隐式默认 n”，而不是展示带一串继承依赖的 `n if ...`。

但 `int`、`hex` 应始终提供默认值，因为它们隐式默认也是空字符串。这样做部分出于与 C 实现 Kconfig 工具兼容；而且对数值项，隐式 `0` 即使可用，也未必符合意图。

一个例外是符号在多处定义，希望靠较早的默认值覆盖后面定义中的默认值。注意：后面的 `default n` 不能覆盖前面已生效的 `default y`。

以下结果为 `n`；如果删掉第一处 `default n`，结果会是 `y`：

```kconfig
config FOO
   bool "foo"
   default n

config FOO
   bool "foo"
   default y
```

交换默认值先后后，结果为 `y`：

```kconfig
config FOO
   bool "foo"
   default y

config FOO
   bool "foo"
   default n
```

## 4.15\_常见缩写与提示风格

`<type> "prompt"` 同时声明类型和提示。以下两种定义等价，Zephyr 推荐第一种：

```kconfig
config FOO
   bool "foo"
```

```kconfig
config FOO
   bool
   prompt "foo"
```

`def_<type> <value>` 同时声明类型和默认值。例如以下两种也等价：

```kconfig
config FOO
   def_bool BAR && BAZ
```

```kconfig
config FOO
   bool
   default BAR && BAZ
```

同一符号同时用这两种缩写会重复声明类型，属于冗余。`def_<type>` 通常只对无提示符号有用，也较不直观。

符号在多处定义时，例如在 `Kconfig.defconfig` 补默认值，最好只在基础定义中给类型，其他位置用 `default`。这样基础定义被删除后，符号缺少类型会产生警告，便于发现并清理遗留定义。

启用驱动或子系统的提示可直接写“Foo”，通常无须写“Enable Foo support”。开关上下文已足够表达启用含义，也更一致。其他格式见[官方代码风格指南](../coding_style/P001_代码风格指南.md#coding-style)。

## 4.16\_imply提供建议而非强制

`imply` 类似 `select`，但尊重依赖、不强制取值。下面让 FOO SoC 默认建议启用 USB 键盘，同时允许用户关闭：

```kconfig
config SOC_FOO
    bool
    imply USB_KEYBOARD

...

config USB_KEYBOARD
     bool "USB keyboard support"
```

区别是：`imply` 提建议，`select` 强制设置。

## 4.17\_可选提示

可以给提示加条件，使一个符号只在部分情况下允许用户配置。例如某些板的掩码固定为 `0xFF`，其他板可修改：

```kconfig
config MASK
     hex "Bitmask" if HAS_CONFIGURABLE_MASK
     default 0xFF
```

等价于：

```kconfig
config MASK
  hex
  prompt "Bitmask" if HAS_CONFIGURABLE_MASK
  default 0xFF
```

板通过选择辅助符号 `HAS_CONFIGURABLE_MASK` 表示掩码可配置；即使允许配置，它仍默认 `0xFF`。

## 4.18\_可选choice

在 choice 中添加 `optional`，允许整组选项关闭，也就是一个成员都不选：

```kconfig
choice
     prompt "Use legacy protocol"
     optional

config LEGACY_PROTOCOL_1
     bool "Legacy protocol 1"

config LEGACY_PROTOCOL_2
     bool "Legacy protocol 2"

endchoice
```

menuconfig 中可能显示 `[*] Use legacy protocol (Legacy protocol 1) --->`。关闭整个选择项后，两个旧协议都不启用。

## 4.19\_visible if只控制可见性

菜单使用 `visible if` 时，可以隐藏菜单及其中所有符号，同时仍让符号的默认值生效。

先看使用普通依赖的版本：

```kconfig
menu "Foo subsystem"
     depends on HAS_CONFIGURABLE_FOO

config FOO_SETTING_1
     int "Foo setting 1"
     default 1

config FOO_SETTING_2
     int "Foo setting 2"
     default 2

endmenu
```

`HAS_CONFIGURABLE_FOO=n` 时，两个设置都不产生配置输出，因为它等价于：

```kconfig
config FOO_SETTING_1
     int "Foo setting 1"
     default 1
     depends on HAS_CONFIGURABLE_FOO

config FOO_SETTING_2
     int "Foo setting 2"
     default 2
     depends on HAS_CONFIGURABLE_FOO
```

如果希望这时仍保留默认值，只是不让用户修改，应改用：

```kconfig
menu "Foo subsystem"
     visible if HAS_CONFIGURABLE_FOO

config FOO_SETTING_1
     int "Foo setting 1"
     default 1

config FOO_SETTING_2
     int "Foo setting 2"
     default 2

endmenu
```

它等价于只限制提示：

```kconfig
config FOO_SETTING_1
     int "Foo setting 1" if HAS_CONFIGURABLE_FOO
     default 1

config FOO_SETTING_2
     int "Foo setting 2" if HAS_CONFIGURABLE_FOO
     default 2
```

因此，`HAS_CONFIGURABLE_FOO=n` 时仍会产生以下输出：

```ini
...
CONFIG_FOO_SETTING_1=1
CONFIG_FOO_SETTING_2=2
...
```

## 4.20\_其他参考

[Kconfiglib 文档字符串](https://github.com/zephyrproject-rtos/Kconfiglib/blob/main/kconfiglib.py)中的 “Intro to symbol values” 一节更详细解释符号值的计算。

> 译注：本章全部示例保留原文符号、英文提示与省略号，中文段落解释其语义；这些用于理解规则的片段不作为完整项目配置直接执行。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：设置 Kconfig 配置值](P003_设置配置值.md) · [本模块主线目录](../reading/kconfig.md) · [全部主线](../reading/README.md) · [下一篇：Kconfig扩展](P005_Kconfig扩展.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：设置配置值](P003_设置配置值.md) · [下一章：Kconfig扩展](P005_Kconfig扩展.md) · [设备树](../devicetree/大纲.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
