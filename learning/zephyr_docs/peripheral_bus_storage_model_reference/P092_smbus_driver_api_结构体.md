---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-92
title: smbus_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_smbus\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：系统管理总线（SMBus）驱动操作。

```c
#include <zephyr/drivers/smbus.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：系统管理总线（SMBus）驱动操作。这是每个 SMBus 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_af023009a650c30d4eb2774f904b20dc1"></a>

```c
smbus_api_configure_t configure
```

相关声明：[smbus_api_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga5fa53c3cd255001a2c34b36a3d23be6f)、[configure](#af023009a650c30d4eb2774f904b20dc1)。

`REQ`：配置 SMBus 主机控制器的运行方式。

<a id="r_a163f4394378189c3b62a7d0edbd7bcf4"></a>

```c
smbus_api_get_config_t get_config
```

相关声明：[smbus_api_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gace2a4372975b44428fb39015e4b4bb25)、[get_config](#a163f4394378189c3b62a7d0edbd7bcf4)。

`OPT`：获取 SMBus 主机控制器的配置。

<a id="r_aa4132b2215173c4856962668344239ef"></a>

```c
smbus_api_quick_t smbus_quick
```

相关声明：[smbus_api_quick_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga93ce314c2797a21ed0b01bb28c69aeaf)、[smbus_quick](#aa4132b2215173c4856962668344239ef)。

`OPT`：执行 SMBus 快速操作（Quick）。

<a id="r_a93f02fcdb7627add8d0e61d34e9d92c4"></a>

```c
smbus_api_byte_write_t smbus_byte_write
```

相关声明：[smbus_api_byte_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga2a59de36841ca4ff5fb65e29c512cd4e)、[smbus_byte_write](#a93f02fcdb7627add8d0e61d34e9d92c4)。

`OPT`：执行 SMBus 字节写操作（Byte Write）。

<a id="r_a9a7c94ae7e2a45ddb80205a2f49aadcd"></a>

```c
smbus_api_byte_read_t smbus_byte_read
```

相关声明：[smbus_api_byte_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gae25c3c8652730085ec31701a48f086b5)、[smbus_byte_read](#a9a7c94ae7e2a45ddb80205a2f49aadcd)。

`OPT`：执行 SMBus 字节读操作（Byte Read）。

<a id="r_a14bb86acc41a9f6ff04a28c763cd1fc9"></a>

```c
smbus_api_byte_data_write_t smbus_byte_data_write
```

相关声明：[smbus_api_byte_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga7827a1f9c5cf8c2b33c79e09d05019ca)、[smbus_byte_data_write](#a14bb86acc41a9f6ff04a28c763cd1fc9)。

`OPT`：执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="r_a6f87df6a6e1357aa4e596a846ab7c84e"></a>

```c
smbus_api_byte_data_read_t smbus_byte_data_read
```

相关声明：[smbus_api_byte_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga36f67cfe281dea020b6036399e433f4a)、[smbus_byte_data_read](#a6f87df6a6e1357aa4e596a846ab7c84e)。

`OPT`：执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="r_a56e1a43e417c7fbae3ac46a844f468fd"></a>

```c
smbus_api_word_data_write_t smbus_word_data_write
```

相关声明：[smbus_api_word_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga31f2a46f83fe193f05cc5494435e2e6f)、[smbus_word_data_write](#a56e1a43e417c7fbae3ac46a844f468fd)。

`OPT`：执行 SMBus 字数据写操作（Word Data Write）。

<a id="r_a1eefcd01d72102861706d426b00a0ef7"></a>

```c
smbus_api_word_data_read_t smbus_word_data_read
```

相关声明：[smbus_api_word_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga94b1bf5e10799ab1f07cccb289033ca6)、[smbus_word_data_read](#a1eefcd01d72102861706d426b00a0ef7)。

`OPT`：执行 SMBus 字数据读操作（Word Data Read）。

<a id="r_a29c68f15c646a9593d128996ed90857e"></a>

```c
smbus_api_pcall_t smbus_pcall
```

相关声明：[smbus_api_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gaabd1e34153c852469e74e9fdc4118c84)、[smbus_pcall](#a29c68f15c646a9593d128996ed90857e)。

`OPT`：执行 SMBus 过程调用（Process Call）。

<a id="r_a5c55f74e8f1b77290c561e2401da105b"></a>

```c
smbus_api_block_write_t smbus_block_write
```

相关声明：[smbus_api_block_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad118b4dc6c7bdea57a6d70240d804b02)、[smbus_block_write](#a5c55f74e8f1b77290c561e2401da105b)。

`OPT`：执行 SMBus 块写操作（Block Write）。

<a id="r_a409d8088579e0ad683dd277ef90f7054"></a>

```c
smbus_api_block_read_t smbus_block_read
```

相关声明：[smbus_api_block_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad7453c161b4fa3c6085c186b39301659)、[smbus_block_read](#a409d8088579e0ad683dd277ef90f7054)。

`OPT`：执行 SMBus 块读操作（Block Read）。

<a id="r_aa96bb1fb738fc8607e6c883ce7cf339c"></a>

```c
smbus_api_block_pcall_t smbus_block_pcall
```

相关声明：[smbus_api_block_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga8e71f105c10414e4ae86b87345e70837)、[smbus_block_pcall](#aa96bb1fb738fc8607e6c883ce7cf339c)。

`OPT`：执行 SMBus 块过程调用（Block Process Call）。

<a id="r_a5e710554c29d1f2c18436558ba8b5eef"></a>

```c
smbus_api_smbalert_cb_t smbus_smbalert_set_cb
```

相关声明：[smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)、[smbus_smbalert_set_cb](#a5e710554c29d1f2c18436558ba8b5eef)。

`OPT`：为 SMBus 主机控制器添加 `SMBALERT` 回调。

<a id="r_a84f25a372c9bffce838dab75dd6d2d57"></a>

```c
smbus_api_smbalert_cb_t smbus_smbalert_remove_cb
```

相关声明：[smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)、[smbus_smbalert_remove_cb](#a84f25a372c9bffce838dab75dd6d2d57)。

`OPT`：从 SMBus 主机控制器移除 `SMBALERT` 回调。

<a id="r_a4649b200f714e74109d9123caff24e7f"></a>

```c
smbus_api_host_notify_cb_t smbus_host_notify_set_cb
```

相关声明：[smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)、[smbus_host_notify_set_cb](#a4649b200f714e74109d9123caff24e7f)。

`OPT`：为 SMBus 主机控制器添加主机通知（Host Notify）回调。

<a id="r_a423f6ecc1ee690c3fde883eccd0b51f7"></a>

```c
smbus_api_host_notify_cb_t smbus_host_notify_remove_cb
```

相关声明：[smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)、[smbus_host_notify_remove_cb](#a423f6ecc1ee690c3fde883eccd0b51f7)。

`OPT`：从 SMBus 主机控制器移除主机通知（Host Notify）回调。

## 92.2\_详细说明（Detailed Documentation）

<a id="af023009a650c30d4eb2774f904b20dc1"></a>

### `configure`

```c
smbus_api_configure_t smbus_driver_api::configure
```

`REQ`：配置 SMBus 主机控制器的运行方式。

<a id="a163f4394378189c3b62a7d0edbd7bcf4"></a>

### `get_config`

```c
smbus_api_get_config_t smbus_driver_api::get_config
```

`OPT`：获取 SMBus 主机控制器的配置。

<a id="aa96bb1fb738fc8607e6c883ce7cf339c"></a>

### `smbus_block_pcall`

```c
smbus_api_block_pcall_t smbus_driver_api::smbus_block_pcall
```

`OPT`：执行 SMBus 块过程调用（Block Process Call）。

<a id="a409d8088579e0ad683dd277ef90f7054"></a>

### `smbus_block_read`

```c
smbus_api_block_read_t smbus_driver_api::smbus_block_read
```

`OPT`：执行 SMBus 块读操作（Block Read）。

<a id="a5c55f74e8f1b77290c561e2401da105b"></a>

### `smbus_block_write`

```c
smbus_api_block_write_t smbus_driver_api::smbus_block_write
```

`OPT`：执行 SMBus 块写操作（Block Write）。

<a id="a6f87df6a6e1357aa4e596a846ab7c84e"></a>

### `smbus_byte_data_read`

```c
smbus_api_byte_data_read_t smbus_driver_api::smbus_byte_data_read
```

`OPT`：执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="a14bb86acc41a9f6ff04a28c763cd1fc9"></a>

### `smbus_byte_data_write`

```c
smbus_api_byte_data_write_t smbus_driver_api::smbus_byte_data_write
```

`OPT`：执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="a9a7c94ae7e2a45ddb80205a2f49aadcd"></a>

### `smbus_byte_read`

```c
smbus_api_byte_read_t smbus_driver_api::smbus_byte_read
```

`OPT`：执行 SMBus 字节读操作（Byte Read）。

<a id="a93f02fcdb7627add8d0e61d34e9d92c4"></a>

### `smbus_byte_write`

```c
smbus_api_byte_write_t smbus_driver_api::smbus_byte_write
```

`OPT`：执行 SMBus 字节写操作（Byte Write）。

<a id="a423f6ecc1ee690c3fde883eccd0b51f7"></a>

### `smbus_host_notify_remove_cb`

```c
smbus_api_host_notify_cb_t smbus_driver_api::smbus_host_notify_remove_cb
```

`OPT`：从 SMBus 主机控制器移除主机通知（Host Notify）回调。

<a id="a4649b200f714e74109d9123caff24e7f"></a>

### `smbus_host_notify_set_cb`

```c
smbus_api_host_notify_cb_t smbus_driver_api::smbus_host_notify_set_cb
```

`OPT`：为 SMBus 主机控制器添加主机通知（Host Notify）回调。

<a id="a29c68f15c646a9593d128996ed90857e"></a>

### `smbus_pcall`

```c
smbus_api_pcall_t smbus_driver_api::smbus_pcall
```

`OPT`：执行 SMBus 过程调用（Process Call）。

<a id="aa4132b2215173c4856962668344239ef"></a>

### `smbus_quick`

```c
smbus_api_quick_t smbus_driver_api::smbus_quick
```

`OPT`：执行 SMBus 快速操作（Quick）。

<a id="a84f25a372c9bffce838dab75dd6d2d57"></a>

### `smbus_smbalert_remove_cb`

```c
smbus_api_smbalert_cb_t smbus_driver_api::smbus_smbalert_remove_cb
```

`OPT`：从 SMBus 主机控制器移除 `SMBALERT` 回调。

<a id="a5e710554c29d1f2c18436558ba8b5eef"></a>

### `smbus_smbalert_set_cb`

```c
smbus_api_smbalert_cb_t smbus_driver_api::smbus_smbalert_set_cb
```

`OPT`：为 SMBus 主机控制器添加 `SMBALERT` 回调。

<a id="a1eefcd01d72102861706d426b00a0ef7"></a>

### `smbus_word_data_read`

```c
smbus_api_word_data_read_t smbus_driver_api::smbus_word_data_read
```

`OPT`：执行 SMBus 字数据读操作（Word Data Read）。

<a id="a56e1a43e417c7fbae3ac46a844f468fd"></a>

### `smbus_word_data_write`

```c
smbus_api_word_data_write_t smbus_driver_api::smbus_word_data_write
```

`OPT`：执行 SMBus 字数据写操作（Word Data Write）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/smbus.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/drivers/smbus.h](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html)
- [smbus_api_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga5fa53c3cd255001a2c34b36a3d23be6f)
- [smbus_api_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gace2a4372975b44428fb39015e4b4bb25)
- [smbus_api_quick_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga93ce314c2797a21ed0b01bb28c69aeaf)
- [smbus_api_byte_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga2a59de36841ca4ff5fb65e29c512cd4e)
- [smbus_api_byte_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gae25c3c8652730085ec31701a48f086b5)
- [smbus_api_byte_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga7827a1f9c5cf8c2b33c79e09d05019ca)
- [smbus_api_byte_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga36f67cfe281dea020b6036399e433f4a)
- [smbus_api_word_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga31f2a46f83fe193f05cc5494435e2e6f)
- [smbus_api_word_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga94b1bf5e10799ab1f07cccb289033ca6)
- [smbus_api_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gaabd1e34153c852469e74e9fdc4118c84)
- [smbus_api_block_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad118b4dc6c7bdea57a6d70240d804b02)
- [smbus_api_block_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad7453c161b4fa3c6085c186b39301659)
- [smbus_api_block_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga8e71f105c10414e4ae86b87345e70837)
- [smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)
- [smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_smbus_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_smbus_dt_spec_结构体.md)
