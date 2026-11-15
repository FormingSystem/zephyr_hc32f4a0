---
id: learning.zephyr-docs.api-guides.api_design
title: API设计指南
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/develop/api/design_guidelines.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_API设计指南

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/api/design_guidelines.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML摘要见[来源记录](../SOURCES.md)。

Zephyr的开发与演进由社区协作完成。为便于维护和增强，新能力和接口应遵循通用规则。**全部公共API必须用Doxygen编写文档**，格式要求见[Doxygen风格指南](../coding_style/P008_Doxygen注释规范.md#doxygen-style)。

## 5.1\_使用回调

许多API通过参数或配置结构体成员接收**回调函数（Callback）**。定义回调签名时应遵循：

1. 第一个参数指向与回调关联最紧密的对象。设备驱动通常使用 `const struct device *dev`；库函数可以指向注册回调时涉及的其他对象。
2. 随后的参数提供本次调用特有的信息，例如通道标识、新状态值，或消息指针和紧随其后的消息长度。
3. 最后一个参数应为 `void *user_data`，携带上下文，使共用回调函数能找到处理所需的附加数据。

如果提供回调的结构体本身嵌入另一个结构体，可允许不把 `user_data` 放在末尾。例如 [`gpio_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html) 通常嵌入定义回调函数的那段代码专用的数据结构；回调可以通过 [`CONTAINER_OF`](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f) 间接获得外层上下文。

### 5.1.1\_示例

系统定时器到期时调用的 [`k_timer_expiry_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html#ga2915762e70454d98c73c179a45cafbde) 可采用：

```c
void handle_timeout(struct k_timer *timer)
{ ... }
```

与GPIO回调类似，这里假定定时器嵌在其他结构中，通过 `CONTAINER_OF` 找到该结构，即可取得附加上下文。

计数器设备报警时调用的 [`counter_alarm_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface.html#ga36c570c3e57e635753d163400e437b77) 可采用：

```c
void handle_alarm(const struct device *dev,
                  uint8_t chan_id,
                  uint32_t ticks,
                  void *user_data)
{ ... }
```

这提供更完整的信息：哪个计数器通道超时、超时时的计数值，以及用户上下文。根据使用需要，上下文可以是注册回调所用的 [`counter_alarm_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structcounter__alarm__cfg.html)，也可以是其他对象。

> 译注：`{ ... }` 表示省略的函数体，是原文签名示意，不是可直接编译的完整实现。

## 5.2\_条件数据与API

API或库可能包含RAM／代码体积开销较大、但部分应用不需要的能力，例如[采集时间戳](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_RX_TIMESTAMP)或[提供另一套接口](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC)。开发者应与社区共同确定是否通过Kconfig选项控制。

确定为可选能力后，应遵循：

- 仅在启用该能力时访问的数据，在结构体或联合体声明中用 `#ifdef CONFIG_MYFEATURE` 条件包含，减少不需要该能力的应用内存占用。
- **函数声明应无条件提供**，即使函数仅在启用选项时可用。文档需明确可用条件，并写出所需Kconfig符号。未启用时，函数定义应排除在编译之外，使错误引用在链接阶段报错。
- 若专用代码单独位于一个没有其他内容的源文件，在 `CMakeLists.txt` 中条件加入该文件：

```cmake
zephyr_sources_ifdef(CONFIG_MYFEATURE foo_funcs.c)
```

- 若专用代码与其他内容同处一个源文件，用 `#ifdef CONFIG_MYFEATURE` 进行条件编译。

如何确保条件代码仍对Doxygen可见并进入公共API文档，见[条件代码文档规则](../coding_style/P008_Doxygen注释规范.md#doxygen-conditional-code)。

## 5.3\_返回码

某个API的实现可能只包含最小运行所需的函数子集，例如访问外设的驱动。需要区分不支持、未实现以及可选能力：

| 情况 | 要求 |
| --- | --- |
| API受支持，但尚未实现 | 返回 `-ENOSYS`。 |
| 硬件不支持某个可选API | 仍应提供实现入口，并返回 `-ENOTSUP`。 |
| API已实现，但无法满足本次调用请求的特定选项组合 | 返回 `-ENOTSUP`。例如硬件仅支持边沿触发，却请求GPIO电平触发中断。 |

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：API生命周期](P004_API生命周期.md) · [本模块主线目录](../reading/api_guides.md) · [全部主线](../reading/README.md) · [下一篇：厂商专用API放置规则](P006_厂商专用API放置规则.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：API生命周期](P004_API生命周期.md) · [下一章：厂商专用API放置规则](P006_厂商专用API放置规则.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
