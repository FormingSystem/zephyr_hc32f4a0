---
id: learning.zephyr-docs.external_modules.page-13
title: Arduino核心API
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/arduino-core-api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="arduino-core-api"></a>
<a id="external-module-arduino-core-api"></a>

# 第13章\_Arduino核心API

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/arduino-core-api.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 13.1\_简介（Introduction）

<a id="id11"></a>

Arduino-Core-Zephyr源于 [2022年Google编程之夏项目](https://dhruvag2000.github.io/Blog-GSoC22/)，为Zephyr实时操作系统（Real-Time Operating System，RTOS）应用提供Arduino风格API。它作为抽象层，让熟悉Arduino的开发者使用Zephyr能力，减少重新学习整套API和库的成本。

<a id="understanding-the-components"></a>

## 13.2\_理解各组件（Understanding the Components）

该模块由两个相互配合的关键组件组成。

### 13.2.1\_ArduinoCore-API：公共API定义（1. ArduinoCore-API (Common Arduino API Definition)）

<a id="id9"></a>

[ArduinoCore-API](https://github.com/arduino/ArduinoCore-API) 是Arduino官方硬件抽象层（Hardware Abstraction Layer，HAL），定义公共Arduino API，包含抽象接口定义与硬件无关功能的实现。

- 同时包含API头文件与硬件无关实现。
- 提供完整实现的 `String`、`Print`、`Stream`、`IPAddress` 等类。
- 定义 `HardwareSerial`、`HardwareSPI` 等硬件相关类的接口。
- 在现代Arduino平台之间共享，保持一致性。
- 实现细节见 [ArduinoCore-API README](https://github.com/arduino/ArduinoCore-API#arduinocore-api)。

该组件采用GNU宽通用公共许可证（GNU Lesser General Public License，LGPL）2.1。

### 13.2.2\_ArduinoCore-Zephyr：Zephyr专用实现（2. ArduinoCore-Zephyr (Zephyr-Specific Implementation)）

<a id="id7"></a>

[Arduino-Core-Zephyr](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr) 提供Arduino API的Zephyr实现，用Zephyr原生API及驱动实现硬件相关函数。

- `cores/arduino` 包含 `zephyrCommon.cpp`、`zephyrSerial.cpp` 等实现。
- 提供开发板变体（Variant）、引脚映射和设备树覆盖文件（Devicetree Overlay）。
- 集成CMake、Kconfig和west.yml等构建入口。
- 链接ArduinoCore-API，复用公共实现。
- 实现细节见 [项目文档](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/tree/main/documentation)。

该组件采用Apache-2.0许可证。

<a id="features-provided"></a>

## 13.3\_提供的功能（Features Provided）

两组件共同提供：

- `pinMode()`、`digitalWrite()`、`analogRead()` 等标准Arduino API。
- Arduino风格的 `setup()` 和 `loop()` 函数。
- Arduino引脚号到Zephyr通用输入输出（General-Purpose Input/Output，GPIO）定义的映射。
- Serial串口、集成电路间总线（Inter-Integrated Circuit，I2C）、串行外设接口（Serial Peripheral Interface，SPI）等常用通信协议。
- 与现有Arduino库的兼容能力。
- Zephyr已有多种硬件平台的开发板变体支持。

这种方式为从Arduino迁移到Zephyr提供更平缓的学习路径，同时保留Zephyr的高级能力、可扩展性和广泛硬件支持。

<a id="usage-with-zephyr"></a>

## 13.4\_在Zephyr中使用（Usage with Zephyr）

<a id="adding-the-arduino-core-api-to-a-zephyr-project"></a>

### 13.4.1\_将Arduino核心API加入Zephyr工程（Adding the Arduino Core API to a Zephyr Project）

在 `west.yml` 中添加west项目，或通过子清单引入，例如 `zephyr/submanifests/arduinocore.yaml`。原条目为：

```yaml
# Arduino API repository
- name: ArduinoCore-zephyr
  path: modules/lib/arduinocore-zephyr
  revision: main
  url: https://github.com/zephyrproject-rtos/ArduinoCore-zephyr
```

> 译注——条目层级：这是单个项目条目，应放在已有清单的 `manifest.projects` 列表下；若新建独立子清单，要自行补上这两级外层键。原注释Arduino API repository表示Arduino API仓库。

更新工程：

```bash
west update
```

Linux用户可使用模块的 `install.sh` 自动链接ArduinoCore-API。不能使用该脚本时，原文要求按后续手工步骤操作。

**注意：**如果 `install.sh` 已成功完成，应跳过下一步；原文将下一步限定为模块安装位置不同或使用自定义Zephyr路径的Linux用户。

原文随后描述“将ArduinoCore-API仓库中的API目录链接进arduinocore-zephyr以完成设置”，给出的命令是：

```bash
west blobs fetch
```

`cores` 目录位于 `<zephyr-project-path>/modules/lib/arduinocore-zephyr/cores`。

> 译注——原文操作不一致：[west blobs实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/scripts/west_commands/blobs.py)用于获取模块元数据声明的二进制对象（Blob）；不能把 `west blobs fetch` 当作创建API目录链接的命令。本次所读[模块元数据](https://raw.githubusercontent.com/zephyrproject-rtos/ArduinoCore-zephyr/main/zephyr/module.yml)也没有声明该API的Blob获取动作。所读[install.sh](https://raw.githubusercontent.com/zephyrproject-rtos/ArduinoCore-zephyr/main/install.sh)则克隆API仓库、修改ArduinoAPI.h中的WCharacter.h包含并创建符号链接，属于不同操作。应按所用版本的安装说明核对链接与头文件是否形成，不以west blobs成功代替验证。本批没有执行这些修改。

<a id="using-arduino-core-api-in-your-application"></a>

### 13.4.2\_在应用中使用Arduino核心API（Using Arduino Core API in Your Application）

<a id="id15"></a>

在应用 `prj.conf` 中，参照 [blinky_arduino示例](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/next/samples/blinky_arduino/prj.conf)启用Arduino API配置。

用Arduino风格代码编写应用：

```cpp
#include <Arduino.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

> 译注——示例行为：setup将 `LED_BUILTIN` 配置为输出，loop依次输出高／低电平，每次等待1000毫秒。实际LED引脚由相应开发板变体定义，不能直接套用其他板的引脚号。

为目标板构建：

```bash
west build -b <board_name> path/to/your/app
```

<a id="adding-custom-board-support"></a>

### 13.4.3\_增加自定义开发板支持（Adding Custom Board Support）

受支持的板位于arduinocore-zephyr的 `variants/`。增加自定义板时：


1. 在 `variants/` 新建以板名命名的目录。

2. 添加与板名匹配的覆盖文件和引脚映射头文件。

3. 在 `variant.h` 的 `#ifdef` 分支中加入新头文件。

<a id="id3"></a>

详细步骤见 [开发板变体文档](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/main/documentation/variants.md)。

<a id="using-external-arduino-libraries"></a>

### 13.4.4\_使用外部Arduino库（Using External Arduino Libraries）

将库源码，例如 `MyLibrary.h`、`MyLibrary.cpp`，加入应用 `src` 目录。在应用 `CMakeLists.txt` 中包含源文件：

```cmake
target_sources(app PRIVATE src/MyLibrary.cpp)
```

然后在代码中包含库头文件：

```cpp
#include "MyLibrary.h"
```

<a id="id5"></a>

更多说明见 [Arduino库文档](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/main/documentation/arduino_libs.md)。

<a id="references"></a>

## 13.5\_参考资料（References）

<a id="id13"></a>

[Arduino-Core-Zephyr仓库](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr)、[ArduinoCore-API仓库](https://github.com/arduino/ArduinoCore-API)及 [Golioth关于Zephyr与Arduino的编程之夏文章](https://blog.golioth.io/zephyr-arduino-a-google-summer-of-code-story/)。

<a id="id2"></a>

1. [开发板变体说明](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/main/documentation/variants.md)。
<a id="id4"></a>

2. [外部库说明](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/main/documentation/arduino_libs.md)。
<a id="id6"></a>

3. [Zephyr实现仓库](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr)。

<a id="id8"></a>

4. [公共API仓库](https://github.com/arduino/ArduinoCore-API)。

<a id="id10"></a>

5. [GSoC 2022项目记录](https://dhruvag2000.github.io/Blog-GSoC22/)。

<a id="id12"></a>

6. [Golioth文章](https://blog.golioth.io/zephyr-arduino-a-google-summer-of-code-story/)。

<a id="id14"></a>

7. [原文引用的next分支示例配置](https://github.com/zephyrproject-rtos/ArduinoCore-zephyr/blob/next/samples/blinky_arduino/prj.conf)。


对应官方文档源码：[doc/develop/manifest/external/arduino-core-api.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/arduino-core-api.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/arduino-core-api.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：IEC60730_B类安全测试](P012_IEC60730_B类安全测试.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：上下文中心运行时CHRE](P014_上下文中心运行时CHRE.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P012_IEC60730_B类安全测试.md) · [返回大纲](大纲.md) · [下一章](P014_上下文中心运行时CHRE.md)

</details>

<!-- reading-navigation:end -->
