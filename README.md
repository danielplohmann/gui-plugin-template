# Binary Analysis Tools Plugin Template

The goal of this template is to provide means for creating GUI plugins compatible with multiple binary analysis tools at once (IDA, Ghidra, Binary Ninja, Cutter) in a convenient fashion.  

It is largely based on the code found in [hyara](https://github.com/hyuunnn/Hyara), which best to our knowledge was the first tool/plugin to achieve such cross-compatibility.  
Therefore, full credit and many thanks to its author [@hyuunnn](https://github.com/hyuunnn) for figuring out many of the irks related to such an endeavor.

## Approach

Common denominator for all platforms is availability of Python and PyQt / PySide in one way or another. 
This allows by separation of concerns to design GUIs that are independent from the concrete binary analysis tools.
"Only" their respective APIs are specific and need to be asbtracted through a common harmonized interface (found in `plugins/apis/`).

Right now the API encapsulation is in an infant state sufficient for demonstration and it will be expanded in future work as we port our own plugins to use this structure.

## Installation and Usage

### IDA Pro

To install as a plugin, copy `PluginIda.py` and folder `plugin` from `template_plugin` to `idapro-x.x/plugins` and simply run from `Edit/Plugins/` or via the assigned hotkey.

### Ghidra

After installing [Ghidraton 4.0](https://github.com/mandiant/Ghidrathon/releases/tag/v4.0.0) and opening its window in Ghidra, we need to manually add our plugin directory to Python's path and then run the plugin:

```
>>> import sys
>>> sys.path.append('/path/to/plugin-template/template_plugin')
>>> import PluginGhidra
>>> PluginGhidra.run()
```

### BinaryNinja

Install as a regular plugin by dropping the full `template_plugin` folder into Binary Ninja [plugins dir](https://github.com/Vector35/binaryninja-api/tree/dev/python/examples#loading-plugins), afterwards run as View/Other Docks/...

### Cutter

TBD.