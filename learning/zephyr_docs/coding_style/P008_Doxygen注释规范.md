---
id: learning.zephyr-docs.coding-style.page-8
title: Doxygen注释规范
kind: reference
status: maintained
domains: [zephyr, documentation, style]
source_url: https://docs.zephyrproject.org/latest/contribute/style/doxygen.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Doxygen注释规范

原文：[官方页面](https://docs.zephyrproject.org/latest/contribute/style/doxygen.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 8.1\_用途与通用规则（General Rules）

Zephyr 使用 [Doxygen](https://www.doxygen.nl/) 从源代码注释生成应用程序编程接口（Application Programming Interface，API）文档。本指南用于保持公共 API 文档的一致性；即使某条 [Doxygen 命令](https://www.doxygen.nl/manual/commands.html)未在本页列出，也可以使用。

在本地构建和预览 Zephyr Doxygen 文档的方法，参见 [文档生成](../contributing/P011_文档生成.md#zephyr-doc)。

所有[公共头文件及其中的公共 API 符号](../getting_started/P006_术语表.md#term-public-API)，包括函数、结构体、枚举、联合体、类型别名、宏和全局变量，都必须满足两项要求：完整编写文档，例外见下文“隐藏内部细节”；至少属于一个 Doxygen 分组（group），见“分组”。

记录公共 API 时，必须使用以下语法：

- 用 `/**` 开始块注释，以 `*/` 结束。
- 与符号位于同一行的尾随注释（trailing comment）使用 `/**<`。
- Doxygen 命令使用 `@`，不用 `\`；例如使用 `@param`，不用 `\param`。
- `@brief` 可省略；省略时，以句点结束的第一句话会被当作简要说明。
- 仅供内部使用的构造必须从公共文档中隐藏，方法见“隐藏内部细节”。

### 8.1.1\_应记录哪些内容（What to Document）

对于接受、返回或保存值的 API 元素，包括函数参数、返回值、结构体／联合体成员、枚举值、类型别名和宏，应在适用时说明以下各项。

**语义（Semantics）。** 说明该元素表示什么，以及调用方或使用方应如何理解它；不要只是复述标识符或 C 类型。例如，应避免 `@param timeout Timeout value in ms.`，它只说“以毫秒为单位的超时值”。推荐 `@param timeout Maximum time to wait before returning, in milliseconds.`，即“返回之前的最长等待时间，单位为毫秒”。

**有效值（Valid Values）。** 说明接受哪些值，以及如何解释这些值。根据情况指定以下一项或多项：

- 范围（range）：最小值、最大值。例如类型虽是 `uint8_t`，有效值却只有 0～100。
- 离散集合（discrete set）：只允许一部分值时，列出允许的值。
- 枚举（enum）：是否必须是某个枚举的合法成员，以及是否允许全部枚举项，还是仅允许其中一部分。
- 标志／位掩码（flags/bitmasks）：哪些位有效，以及能否组合。
- 可空性（nullability）：指针是否允许为 `NULL`，以及为空时的含义。

**单位（Units）。** 值表示数量时，说明单位及参照，例如毫秒还是时钟节拍（tick）、赫兹或字节。在适用时使用国际单位制（SI）单位符号，数字与单位之间保留空格，例如 `10 ms`。

**表示形式（Representation）。** 说明不直观的编码或缩放规则，例如定点缩放、Q 格式、分开的整数与小数字段，以及字节序（endianness）要求。

**所有权与生命周期（Ownership and Lifetime）。** 对指针或缓冲区，说明由谁分配、由谁释放，以及内存需要保持有效多久；相关时还应说明大小和对齐要求。

### 8.1.2\_写作风格（Writing Style）

简要说明应采用祈使语气的动词短语，而不是第三人称叙述，使 API 摘要一致、便于浏览。

- 避免：`Transmits data through a pipe.`，即“它通过管道传输数据”；`This function gets the device state.`，即“此函数获取设备状态”。
- 推荐：`Transmit data through a pipe.`，即“通过管道传输数据”；`Get the device state.`，即“获取设备状态”；`Initialize the subsystem.`，即“初始化子系统”。

参数和成员的说明可以是不完整句，但仍应具有描述性，避免只重复参数名或成员名。

## 8.2\_分组（Groups）

分组将相关符号组织成层次结构，帮助使用者浏览 API。

- 每个组只用 `@defgroup` 定义一次。
- 组标题使用简短且具有描述性的名称。分组本身已经汇集了各种接口或 API，因此标题不要再使用 `API`、`Interface` 或这些词的其他变体，以免重复。
- 组的简要说明不要只是换一种说法重复组标题。
- 组名称使用[蛇形命名法（snake_case）](https://en.wikipedia.org/wiki/Snake_case)。
- 使用 `@ingroup` 指定该组所属的一个或多个父组。

示例：

```c
/**
 * @defgroup mqtt_socket MQTT Client library
 * @ingroup networking
 * @since 1.14
 * @version 0.8.0
 * @{
 */

 /* documented contents of the MQTT header file */

 /** @} */
```

> 示例文字译文：`MQTT Client library` 为“MQTT 客户端库”；中间的注释表示“MQTT 头文件中已编写文档的内容”。分组命令和标识符保持原样。

> 注意：一个组可以属于多个父组，所以可以使用多条 `@ingroup`。例如，设备驱动仿真器通常同时出现在“仿真器接口（Emulator Interfaces）”和“设备驱动（Device drivers）”分组中，参见 [I2C 仿真接口](../hardware/P314_I2C模拟后端.md)。

> 重要：没有父组的组会成为 [API 总览](../api_guides/P002_API概览.md#api-overview)中的顶层条目；顶层分类的数量是刻意控制的。新增分组时，始终用 `@ingroup` 指定父组。
>
> 顶层条目通过 [`doc/_doxygen/toplevel_groups.txt`](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_doxygen/toplevel_groups.txt) 中的允许列表管理，由 [`scripts/ci/doxygen_toplevel_groups.py`](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/ci/doxygen_toplevel_groups.py) 检查执行。新增顶层条目需要文档维护者批准。

## 8.3\_API 版本管理（API Versioning）

在分组定义 `@defgroup` 上使用 `@since` 和 `@version` 记录 API 的历史与成熟度：

- `@since` 表示引入该 API 时的 Zephyr 发行版本，例如 `@since 3.7`。
- `@version` 表示当前 API 版本，采用语义化版本（semantic versioning）。

版本号反映的 API 成熟度定义见 [API 总览](../api_guides/P002_API概览.md#api-overview)。

以下示例表示 API 在 Zephyr 1.14 中引入，当前版本为 0.8.0，处于不稳定状态（unstable）。

```c
/**
 * @defgroup mqtt_socket MQTT Client library
 * @ingroup networking
 * @since 1.14
 * @version 0.8.0
 * @{
 */

 /* documented contents of the MQTT header file */

 /** @} */
```

该例中的库名称和占位注释与上一节相同，分别为“MQTT 客户端库”和“MQTT 头文件中已编写文档的内容”。

## 8.4\_文件（Files）

每个公共头文件顶部都必须有 `@file` 注释块，放在 SPDX 许可证与版权声明之后。

`@file` 注释块还必须属于某个 Doxygen 组，通常就是同一头文件中定义的组。这使按文件浏览的使用者能够方便地跳转到关联分组。

```c
/**
 * @file
 * @brief Public API for the GPIO driver.
 * @ingroup gpio_interface
 */
```

示例的简要说明为“通用输入输出（General-Purpose Input/Output，GPIO）驱动的公共 API”，所属分组是 `gpio_interface`。

## 8.5\_类型定义（Type Definitions）

为 `struct`、`enum`、`union` 和 `typedef` 定义编写简要说明。每个成员，包括结构体字段、枚举值等，也必须有文档。如果只需要简要说明且一行能放下，推荐使用 `/**<` 尾随注释。

以下是完整记录枚举、结构体和类型别名的示例：

```c
/** @brief Parity modes */
enum uart_config_parity {
     UART_CFG_PARITY_NONE,   /**< No parity */
     UART_CFG_PARITY_ODD,    /**< Odd parity */
     UART_CFG_PARITY_EVEN,   /**< Even parity */
     UART_CFG_PARITY_MARK,   /**< Mark parity */
     UART_CFG_PARITY_SPACE,  /**< Space parity */
};

/**
 * GPIO pin configuration.
 *
 * Specifies direction, pull resistor, and interrupt settings.
 */
struct gpio_config {
    uint32_t flags;    /**< Pin configuration flags. */
    gpio_pin_t pin;    /**< Pin number within the port. */
};

/**
 * @brief Identifies a set of pins associated with a port.
 *
 * The pin with index n is present in the set if and only if the bit
 * identified by (1U << n) is set.
 */
typedef uint32_t gpio_port_pins_t;
```

示例注释译文如下：

| 对象 | 注释内容 |
| --- | --- |
| `uart_config_parity` | 奇偶校验模式（parity mode）。各枚举项依次为无校验、奇校验、偶校验、标记校验（Mark parity）、空格校验（Space parity）。 |
| `gpio_config` | GPIO 引脚配置；指定方向、上拉／下拉电阻和中断设置。 |
| `flags` | 引脚配置标志。 |
| `pin` | 端口内的引脚编号。 |
| `gpio_port_pins_t` | 标识与某个端口关联的一组引脚。当且仅当 `(1U << n)` 对应的位被置位时，索引为 `n` 的引脚才在集合中。 |

## 8.6\_函数（Functions）

### 8.6.1\_参数（Parameters）

- 按声明顺序，使用 `@param` 记录参数。
- 对函数会写入的指针使用 `@param[out]`。
- 对函数既读取又写入的指针使用 `@param[in,out]`。
- 对 `const` 指针和标量，可以省略方向标记；它们隐含为只输入。

### 8.6.2\_返回值（Return Values）

- 通用说明使用 `@return <description>`，例如布尔值或计算结果。
- 具体的离散返回值通常是错误码，使用 `@retval <value> <description>`；适用时先列成功情况。第一个词必须是返回值，后接说明。例如用 `@retval -EINVAL Invalid arguments`，不用 `@retval -EINVAL if invalid arguments`。

> 注意：同一个离散返回值可能有多个原因，因此允许多条 `@retval` 使用相同的返回值。

以下示例完整记录了函数：

```c
/**
 * @brief Write data to the TX queue from a provided buffer
 *
 * @param dev Pointer to the device structure for the driver instance.
 * @param buf Pointer to a buffer containing the data to transmit.
 * @param size Number of bytes to write. This value has to be equal or smaller
 *        than the size of the channel's TX memory block configuration.
 *
 * @retval 0 on success.
 * @retval -EIO The interface is not in READY or RUNNING state.
 * @retval -EBUSY Returned without waiting.
 * @retval -EAGAIN Waiting period timed out.
 * @retval -ENOMEM No memory in TX slab queue.
 * @retval -EINVAL Size parameter larger than TX queue memory block.
 */
int i2s_buf_write(const struct device *dev, void *buf, size_t size);

/**
 * @brief Add an application callback.
 *
 * @param port Pointer to the device structure for the driver instance.
 * @param callback A valid application's callback structure pointer.
 *
 * @return 0 on success, negative errno value on failure.
 * @retval -ENOSYS Driver does not implement the operation.
 */
int gpio_add_callback(const struct device *port, struct gpio_callback *callback);

/**
 * @brief Helper function for converting struct sensor_value to float.
 *
 * @param val A pointer to a sensor_value struct.
 * @return The converted value.
 */
static inline float sensor_value_to_float(const struct sensor_value *val)
{
    return (float)val->val1 + (float)val->val2 / 1000000;
}
```

原例注释逐项译文：

**`i2s_buf_write`：从提供的缓冲区向发送（TX）队列写入数据。**

| 参数或返回值 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构体。 |
| `buf` | 指向包含待发送数据的缓冲区。 |
| `size` | 要写入的字节数，必须小于或等于该通道所配置的 TX 内存块大小。 |
| `0` | 成功。 |
| `-EIO` | 接口不处于 `READY` 或 `RUNNING` 状态。 |
| `-EBUSY` | 未等待便返回。 |
| `-EAGAIN` | 等待超时。 |
| `-ENOMEM` | TX 内存块队列（slab queue）中没有可用内存。 |
| `-EINVAL` | `size` 参数大于 TX 队列内存块大小。 |

**`gpio_add_callback`：添加应用程序回调（callback）。** `port` 指向驱动实例的设备结构体；`callback` 是有效的应用回调结构体指针。成功返回 0，失败返回负的 `errno` 值；驱动没有实现该操作时返回 `-ENOSYS`。

**`sensor_value_to_float`：将 `struct sensor_value` 转换为 `float` 的辅助函数。** `val` 是指向 `sensor_value` 结构体的指针；返回转换后的值。

## 8.7\_宏（Macros）

函数式宏（function-like macro）的参数应像函数参数一样编写文档。以下是完整示例：

```c
/**
 * @brief Get a node's (only) register block size
 *
 * Equivalent to DT_REG_SIZE_BY_IDX(node_id, 0).
 *
 * @param node_id node identifier
 * @return node's only register block's size
 */
#define DT_REG_SIZE(node_id) DT_REG_SIZE_BY_IDX(node_id, 0)
```

示例注释译文：取得节点唯一寄存器块的大小；等价于 `DT_REG_SIZE_BY_IDX(node_id, 0)`。`node_id` 是节点标识符；返回节点唯一寄存器块的大小。

## 8.8\_引用主文档（Referencing the Main Documentation）

API 文档可以通过以下命令引用基于 Sphinx 的主文档内容。在生成的 API 页面中，这些引用会显示为超链接，指向主文档中的相应页面。

### 8.8.1\_Kconfig 选项

`@kconfig{<option>}` 按完整名称引用一个 Kconfig 选项，名称包含 `CONFIG_` 前缀。它对应 Sphinx 的 [`kconfig:option` 角色（role）](../contributing/P010_文档编写指南.md#role-kconfig-option)。

示例：`@kconfig{CONFIG_GPIO}`。

`@kconfig_regex{<regex>}` 引用匹配某个正则表达式（regular expression）的全部 Kconfig 选项，生成的链接进入 Kconfig 搜索页，并预先填入该表达式。它对应 [`kconfig:option-regex` 角色](../contributing/P010_文档编写指南.md#role-kconfig-option-regex)。逗号在 Doxygen 命令中具有特殊含义，必须用反斜杠转义。

示例：`@kconfig_regex{CONFIG_SECURE_STORAGE_ITS_.*_CUSTOM}`。

### 8.8.2\_设备树绑定

`@dtcompatible{<compatible>}` 按兼容字符串（compatible string）引用设备树绑定（Devicetree binding），对应 [`dtcompatible` 角色](../contributing/P010_文档编写指南.md#role-dtcompatible)。同样，因为逗号具有特殊含义，必须用反斜杠转义。

示例：`@dtcompatible{zephyr\,input-longpress}`。

### 8.8.3\_文档页面或章节

`@rstref{<target>}` 或 `@rstref{<text> <target>}` 按引用标签或文档名称引用任意页面或章节，与 Sphinx 的 `ref` 角色类似。不提供自定义文字时，使用被引用页面或章节的标题作为链接文字。

示例：`@rstref{zephyr_licensing}`，或 `@rstref{the licensing page <zephyr_licensing>}`；后者的自定义文字表示“许可说明页面”。

构建文档时会检查引用。如果指向不存在的 Kconfig 选项、绑定或标签，会产生文档构建警告。

> 注意：仅单独构建 Doxygen 文档、不构建其余主文档时，这些命令展开为纯文本。详细说明见 [文档生成](../contributing/P011_文档生成.md#zephyr-doc)。

## 8.9\_引用IETF RFC（Referencing IETF RFCs）

`@rfc{<number>}` 或 `@rfc{<number>,<anchor>}` 按编号引用互联网工程任务组（Internet Engineering Task Force，IETF）的 RFC 文档，并可选择指定其中的锚点。它对应 Sphinx 的 `rfc` 角色，生成指向 IETF Datatracker 上相应 RFC 的超链接。

锚点（anchor）会原样传递，因此可以指向 Datatracker 为该 RFC 定义的任何锚点，例如 `section-3.1`、`appendix-B.1.2`、`figure-2` 或 `table-1`。实际有哪些锚点取决于 RFC 本身：只有从 XML 源文件渲染的 RFC 才为图和表提供锚点。

不要在逗号后添加空白。Doxygen 会把空白保留为参数的一部分，最终进入 URL 片段。链接显示文字看起来仍然正确，只有点击时才会发现锚点无法跳转。

示例：`@rfc{7519}`、`@rfc{8613,section-3.1}` 或 `@rfc{8613,appendix-B.1.2}`。

## 8.10\_隐藏内部细节（Hiding Internal Details）

使用 `@cond INTERNAL_HIDDEN` 与 `@endcond` 从生成文档中隐藏内部细节。仍可选择为这些内部符号编写注释，为内部使用者提供参考。

```c
/** Timer structure.
 *
 * Opaque type for a timer object. All the fields in this structure are internal and should not
 * be accessed outside of kernel code.
 */
struct k_timer {
    /** @cond INTERNAL_HIDDEN */

    /* ... internal members ... */

    /** @endcond */
};
```

示例注释译文：“定时器结构体。定时器对象的不透明类型（opaque type）；所有字段均为内部字段，不应在内核代码之外访问。”中间占位注释表示“内部成员”。

## 8.11\_驱动后端API（Driver Backend API）

驱动子系统为应用程序提供公共 API，同时为驱动实现者提供“后端（backend）”API。

后端 API 虽然不供应用直接使用，仍构成子系统与驱动实现者之间的公共契约，因此必须有适当的文档。它通常包括驱动操作结构体、定义各操作函数签名的类型别名，有时还包含对驱动实现有用的辅助类型或宏。

### 8.11.1\_后端API分组（Backend API Doxygen Group）

使用 `@def_driverbackendgroup` 创建主 API 组的子组，容纳所有后端 API 相关符号。该命令有两个参数：便于阅读的后端 API 名称，通常与父组名称相同；以及父组标识符。

```c
/**
 * @def_driverbackendgroup{Haptics,haptics_interface}
 * @{
 */

/* callback typedefs, driver ops struct, helpers ... */

/** @} */
```

例中的 `Haptics` 表示“触觉反馈”；中间注释表示“回调类型别名、驱动操作结构体、辅助项等”。

### 8.11.2\_驱动操作类型别名（Driver Operations Typedefs）

为每项驱动操作定义一个类型别名（typedef）。由于函数签名通常相似，详细说明可以引用对应的公共 API 函数。

```c
/**
 * @brief Set the haptic device to stop output.
 * See haptics_stop_output() for argument description.
 */
typedef int (*haptics_stop_output_t)(const struct device *dev);
```

示例注释译文：“使触觉反馈设备停止输出。参数说明参见 `haptics_stop_output()`。”

### 8.11.3\_驱动操作结构体（Driver Operations Structure）

为结构体添加 `@driver_ops{Name}`，其中 `Name` 与传给 `@def_driverbackendgroup` 的名称一致。每个成员使用 `@driver_ops_mandatory` 或 `@driver_ops_optional` 指明驱动是否必须实现该操作，并用 `@copybrief` 继承公共 API 函数的简要说明：

```c
/**
 * @driver_ops{Haptics}
 */
__subsystem struct haptics_driver_api {
    /**
     * @driver_ops_mandatory @copybrief haptics_start_output
     */
    haptics_start_output_t start_output;
    /**
     * @driver_ops_mandatory @copybrief haptics_stop_output
     */
    haptics_stop_output_t stop_output;
    /**
     * @driver_ops_optional @copybrief haptics_register_error_callback
     */
    haptics_register_error_callback_t register_error_callback;
};
```

例中 `start_output` 和 `stop_output` 是必选操作（mandatory）；`register_error_callback` 是可选操作（optional）。各项简要说明分别继承对应的公共函数。

## 8.12\_条件编译代码（Conditional Code）

要让条件编译的代码出现在文档中，可以采用以下任一方法：

- 将控制该代码的 Kconfig 宏 `CONFIG_...` 加入 [`doc/zephyr.doxyfile.in`](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/zephyr.doxyfile.in) 中的 `PREDEFINED` 列表，使 Doxygen 在生成文档时可见这段代码。
- 利用 Doxygen 自动定义的 `__DOXYGEN__` 宏，使条件编译代码对 Doxygen 可见。

```c
struct coap_packet {
    uint8_t *data;  /**< User allocated buffer. */
#if defined(CONFIG_COAP_KEEP_USER_DATA) || defined(__DOXYGEN__)
    /**
     * Application-specific user data.
     * @kconfig_dep{CONFIG_COAP_KEEP_USER_DATA}
     */
    void *user_data;
#endif
};
```

示例注释译文：`data` 是“用户分配的缓冲区”；`user_data` 是“应用专用的用户数据”，并通过 `@kconfig_dep{CONFIG_COAP_KEEP_USER_DATA}` 说明配置依赖。

## 8.13\_Kconfig依赖（Kconfig Dependencies）

`@kconfig_dep` 用于记录：要使某个 API 符号可供使用，必须启用哪些 Kconfig 选项。该命令支持一个、两个或三个选项。

例如，在 API 符号的 Doxygen 注释中添加 `@kconfig_dep{CONFIG_PM,CONFIG_SMP}`，生成的文档就会包含提示：“仅在以下 Kconfig 选项启用时可用：`CONFIG_PM`、`CONFIG_SMP`。”

[`coap_packet` 文档](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__packet.html)中也有 `@kconfig_dep` 的使用示例。


对应官方文档源码：[doc/contribute/style/doxygen.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/contribute/style/doxygen.rst)。

本仓库的[对应源码](../../../doc/contribute/style/doxygen.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="doxygen-style-guidelines"></a>
<a id="doxygen-style"></a>
<a id="general-rules"></a>
<a id="what-to-document"></a>
<a id="writing-style"></a>
<a id="groups"></a>
<a id="doxygen-groups"></a>
<a id="api-versioning"></a>
<a id="doxygen-api-versioning"></a>
<a id="id1"></a>
<a id="files"></a>
<a id="type-definitions"></a>
<a id="id2"></a>
<a id="functions"></a>
<a id="parameters"></a>
<a id="return-values"></a>
<a id="id3"></a>
<a id="macros"></a>
<a id="id4"></a>
<a id="referencing-the-main-documentation"></a>
<a id="doxygen-sphinx-xrefs"></a>
<a id="referencing-ietf-rfcs"></a>
<a id="doxygen-rfc-refs"></a>
<a id="hiding-internal-details"></a>
<a id="doxygen-internals"></a>
<a id="driver-backend-api"></a>
<a id="doxygen-driver-backend"></a>
<a id="backend-api-doxygen-group"></a>
<a id="driver-operations-typedefs"></a>
<a id="driver-operations-structure"></a>
<a id="conditional-code"></a>
<a id="doxygen-conditional-code"></a>
<a id="kconfig-dependencies"></a>
<a id="doxygen-kconfig-dep"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Python编码风格](P007_Python编码风格.md) · [本模块主线目录](../reading/coding_style.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_Python编码风格.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
