---
id: learning.zephyr-docs.external_modules.page-27
title: WebAssembly微运行时WAMR
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/wamr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="webassembly-micro-runtime-wamr"></a>
<a id="external-module-wamr"></a>

# 第27章\_WebAssembly微运行时WAMR

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/wamr.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 27.1\_简介（Introduction）

<a id="id2"></a>

<a id="id4"></a>

[WebAssembly微运行时（WebAssembly Micro Runtime，WAMR）](https://github.com/wasm-micro-runtime/wasm-micro-runtime)是面向嵌入式和资源受限设备的轻量独立运行时，可在运行时加载、执行WebAssembly（WASM）模块，无须重新烧录固件即可更新或扩展功能，并在WASM规范定义的沙箱（Sandbox）内运行不可信代码。运行时API、执行模式及 `wamrc` 提前编译（Ahead-of-Time，AOT）编译器见 [WAMR文档](https://github.com/wasm-micro-runtime/wasm-micro-runtime/tree/main/doc)。

WAMR通过专用平台层支持Zephyr，仓库内自带 `zephyr/module.yml`、`zephyr/Kconfig` 和 `zephyr/CMakeLists.txt` 等接入文件，应用选择若干Kconfig选项即可把运行时链接到镜像中。

WAMR采用带LLVM例外条款的Apache License 2.0。

<a id="usage-with-zephyr"></a>

## 27.2\_在Zephyr中使用（Usage with Zephyr）

将以下条目加入子清单，例如 `zephyr/submanifests/wamr.yaml`，然后运行 `west update`；也可直接合并进应用 `west.yml` 的项目列表：

```yaml
manifest:
  projects:
    - name: wasm-micro-runtime
      url: https://github.com/wasm-micro-runtime/wasm-micro-runtime
      revision: main
      path: modules/wasm-micro-runtime # adjust the path as needed
```

<a id="configuring-the-runtime"></a>

### 27.2.1\_配置运行时（Configuring the runtime）

运行时默认关闭。在应用 `prj.conf` 用 `CONFIG_WAMR_*` 选项启用并选择功能：

```kconfig
CONFIG_WAMR=y
CONFIG_WAMR_INTERP=y
CONFIG_WAMR_AOT=y
CONFIG_WAMR_LIBC_BUILTIN=y
CONFIG_WAMR_GLOBAL_HEAP_POOL=y
CONFIG_WAMR_GLOBAL_HEAP_SIZE=131072
```

每个选项映射到常规WAMR构建脚本的相应 `WAMR_BUILD_*` CMake变量，也可以在单次构建时通过命令行覆盖，例如 `-DWAMR_BUILD_AOT=0`。

<a id="id6"></a>

`WAMR_BUILD_TARGET` 从开发板架构推导，通常无需传入。仓库随附 [Zephyr示例](https://github.com/wasm-micro-runtime/wasm-micro-runtime/tree/main/product-mini/platforms/zephyr)，构建与运行方法见其 `README.md`。

<a id="reference"></a>

## 27.3\_参考资料（Reference）


<a id="id1"></a>

1. [WAMR仓库](https://github.com/wasm-micro-runtime/wasm-micro-runtime)。

<a id="id3"></a>

2. [WAMR文档](https://github.com/wasm-micro-runtime/wasm-micro-runtime/tree/main/doc)。

<a id="id5"></a>

3. [Zephyr示例](https://github.com/wasm-micro-runtime/wasm-micro-runtime/tree/main/product-mini/platforms/zephyr)。


对应官方文档源码：[doc/develop/manifest/external/wamr.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/wamr.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；本批仅翻译和核对文档。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Thrift](P026_Thrift.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Xedge](P028_Xedge.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P026_Thrift.md) · [返回大纲](大纲.md) · [下一章](P028_Xedge.md)

</details>

<!-- reading-navigation:end -->
