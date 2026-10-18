---
id: learning.zephyr-docs.api-file-reference.page-492
title: zephyr__posix__unistd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第492章\_zephyr\_\_posix\_\_unistd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <time.h>
#include <zephyr/posix/posix_types.h>
#include <zephyr/posix/sys/confstr.h>
#include <zephyr/posix/sys/stat.h>
#include <zephyr/posix/sys/sysconf.h>
#include "posix_features.h"
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 492.1\_函数（Functions）

<a id="r_a5d88641f86c8a447fefd1e531758a3c0"></a>

```c
int getentropy (void *buffer, size_t length)
```

相关声明：[getentropy](#a5d88641f86c8a447fefd1e531758a3c0)。

<a id="r_ac61b207337ca21b3b309593fd1a0cb82"></a>

```c
pid_t getpid (void)
```

相关声明：[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)、[getpid](#ac61b207337ca21b3b309593fd1a0cb82)。

<a id="r_aaa1de6debea33c41fbfaa909e813c2f4"></a>

```c
unsigned sleep (unsigned int seconds)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[sleep](#aaa1de6debea33c41fbfaa909e813c2f4)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a59715f1a0a2ee4dc75e8343aca15c1dd"></a>

```c
int usleep (useconds_t useconds)
```

相关声明：[usleep](#a59715f1a0a2ee4dc75e8343aca15c1dd)、[useconds_t](P312_zephyr__posix__posix_types.h_文件参考.md#a1cf3c794977f92f3ccf2e041a68f3342)。

<a id="r_a599f55d9eaa01b6921367233437b9b13"></a>

```c
long sysconf (int opt)
```

相关声明：[sysconf](#a599f55d9eaa01b6921367233437b9b13)。

## 492.2\_详细说明（Detailed Documentation）

<a id="a5d88641f86c8a447fefd1e531758a3c0"></a>

### `getentropy()`

```c
int getentropy ( void * buffer, size_t length )
```

<a id="ac61b207337ca21b3b309593fd1a0cb82"></a>

### `getpid()`

```c
pid_t getpid ( void )
```

<a id="aaa1de6debea33c41fbfaa909e813c2f4"></a>

### `sleep()`

```c
unsigned sleep ( unsigned int seconds)
```

<a id="a599f55d9eaa01b6921367233437b9b13"></a>

### `sysconf()`

```c
long sysconf ( int opt)
```

<a id="a59715f1a0a2ee4dc75e8343aca15c1dd"></a>

### `usleep()`

```c
int usleep ( useconds_t useconds)
```


## 492.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [zephyr/posix/sys/confstr.h](../api_source_reference/P112_confstr.h_源码浏览.md)
- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [zephyr/posix/sys/sysconf.h](../api_source_runtime_reference/P063_sysconf.h_源码浏览.md)
- [posix_features.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__features_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P116_unistd.h_源码浏览.md)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [useconds_t](P312_zephyr__posix__posix_types.h_文件参考.md#a1cf3c794977f92f3ccf2e041a68f3342)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P491_zephyr__net__udp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P493_zephyr__posix__sys__utsname.h_文件参考.md)
