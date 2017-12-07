""" This file is only used to generate documentation """

# VM class
class vm():    
    def getGPRState():
        """Obtain the current general purpose register state.
        
            :returns: gprState -- A structure containing the GPR state.
        """
        pass
    def getFPRState():
        """Obtain the current floating point register state.
        
            :returns: gprState : A structure containing the FPR state.
        """
        pass
    def setGPRState(gprState):
        """Set the GPR state.
            
            :param grpState: A structure containing the GPR state.
        """
        pass
    def setFPRState(fprState):
        """Obtain the current floating point register state.
        
            :param fprState: A structure containing the FPR state
        """
        pass
    
    def run(start, stop):
        """Start the execution by the DBI from a given address (and stop when another is reached).
        
            :param start: Address of the first instruction to execute.
            :param stop: Stop the execution when this instruction is reached.
            
            :returns: True if at least one block has been executed.
        """
        pass
    def call(function, args):
        """Call a function using the DBI (and its current state).
        
            :param function: Address of the function start instruction.
            :param args: The arguments as dictionary {0:arg0, 1:arg1, 2:arg2, ...}.
            
            :returns: (True, retValue) if at least one block has been executed.
        """
        pass
    def addCodeCB(pos, cbk, data):
        """Register a callback event for a specific instruction event.
            
            :param pos: Relative position of the event callback (pyqbdi.PREINST / pyqbdi.POSTINST).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addCodeAddrCB(address, pos, cbk, data):
        """Register a callback for when a specific address is executed.
        
            :param address: Code address which will trigger the callback.
            :param pos: Relative position of the event callback (pyqbdi.PREINST / pyqbdi.POSTINST).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addCodeRangeCB(start, end, pos, cbk, data):
        """Register a callback for when a specific address range is executed.
            
            :param start: Start of the address range which will trigger the callback.
            :param end: End of the address range which will trigger the callback.
            :param pos: Relative position of the event callback (pyqbdi.PREINST / pyqbdi.POSTINST).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addMnemonicCB(mnemonic, pos, cbk, data):
        """Register a callback event if the instruction matches the mnemonic.
        
            :param mnemonic: Mnemonic to match.
            :param pos: Relative position of the event callback (pyqbdi.PREINST / pyqbdi.POSTINST).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def deleteInstrumentation(id):
        """Remove an instrumentation.
            
            :param id: The id of the instrumentation to remove.
            
            :returns: True if instrumentation has been removed.
        """
        pass
    def deleteAllInstrumentations():
        """Remove all the registered instrumentations.
        """
        pass
    
    def addMemAddrCB(address, type, cbk, data):
        """Add a virtual callback which is triggered for any memory access at a specific address matching the access type. Virtual callbacks are called via callback forwarding by a gate callback triggered on every memory access. This incurs a high performance cost.
        
            :param address: Code address which will trigger the callback.
            :param type: A mode bitfield: either pyqbdi.MEMORY_READ, pyqbdi.MEMORY_WRITE or both (pyqbdi.MEMORY_READ_WRITE).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns:  The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addMemRangeCB(start, end, type, cbk, data):
        """Add a virtual callback which is triggered for any memory access in a specific address range matching the access type. Virtual callbacks are called via callback forwarding by a gate callback triggered on every memory access. This incurs a high performance cost.
        
            :param start: Start of the address range which will trigger the callback.
            :param end: End of the address range which will trigger the callback.
            :param type: A mode bitfield: either pyqbdi.MEMORY_READ, pyqbdi.MEMORY_WRITE or both (pyqbdi.MEMORY_READ_WRITE).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns:  The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addMemAccessCB(type, cbk, data):
        """Register a callback event for every memory access matching the type bitfield made by an instruction.
        
            :param type: A mode bitfield: either pyqbdi.MEMORY_READ, pyqbdi.MEMORY_WRITE or both (pyqbdi.MEMORY_READ_WRITE).
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def recordMemoryAccess(type):
        """Add instrumentation rules to log memory access using inline instrumentation and instruction shadows.
        
            :param type: Memory mode bitfield to activate the logging for: either pyqbdi.MEMORY_READ, pyqbdi.MEMORY_WRITE or both (pyqbdi.MEMORY_READ_WRITE).
            
            :returns: True if inline memory logging is supported, False if not or in case of error.
        """
        pass

    def getInstAnalysis(type):
        """ Obtain the analysis of an instruction metadata. Analysis results are cached in the VM. The validity of the returned pointer is only guaranteed until the end of the callback, else  a deepcopy of the structure is required.
        
            :param type: Properties to retrieve during analysis.
            
            :returns: A InstAnalysis structure containing the analysis result.
        """
        pass
    def getInstMemoryAccess():
        """Obtain the memory accesses made by the last executed instruction.
        
            :returns: An array of memory accesses made by the instruction.
        """
        pass
    def getBBMemoryAccess():
        """Obtain the memory accesses made by the last executed basic block.
        
            :returns: An array of memory accesses made by the basic block.
        """
        pass

    def precacheBasicBlock(pc):
        """Pre-cache a known basic block
        
            :param pc: Start address of a basic block
            
            :returns: True if basic block has been inserted in cache.
        """
        pass
    def clearCache(start, end):
        """Clear a specific address range from the translation cache.
        
            :param start: Start of the address range to clear from the cache.
            :param end: End of the address range to clear from the cache.
        """
        pass
    def clearAllCache():
        """Clear the entire translation cache.
        """
        pass

    def addVMEventCB(mask, cbk, data):
        """Register a callback event for a specific VM event.
        
            :param mask: A mask of VM event type which will trigger the callback.
            :param cbk: A function pointer to the callback.
            :param data: User defined data passed to the callback.
            
            :returns: The id of the registered instrumentation (or pyqbdi.INVALID_EVENTID in case of failure).
        """
        pass
    def addInstrumentedModule(name):
        """Add the executable address ranges of a module to the set of instrumented address ranges.
        
            :param name: The module's name.
            
            :returns: True if at least one range was added to the instrumented ranges.
        """
        pass
    def addInstrumentedModuleFromAddr(addr):
        """ Add the executable address ranges of a module to the set of instrumented address ranges using an address belonging to the module.
        
            :param addr: An address contained by module's range.
            
            :returns: True if at least one range was added to the instrumented ranges.
        """
        pass
    def addInstrumentedRange(start, end):
        """Add an address range to the set of instrumented address ranges.
        
            :param start: Start address of the range (included).
            :param end: End address of the range (excluded).
            
        """
        pass
    def instrumentAllExecutableMaps():
        """Adds all the executable memory maps to the instrumented range set.
        
            :returns: True if at least one range was added to the instrumented ranges.
        """
        pass
    def removeAllInstrumentedRanges():
        """Remove all instrumented ranges.
        """
        pass
    def removeInstrumentedModule(name):
        """Remove the executable address ranges of a module from the set of instrumented address ranges.
        
            :param name: The module's name.
            
            :returns: True if at least one range was removed from the instrumented ranges.
        """
        pass
    def removeInstrumentedModuleFromAddr(addr):
        """Remove the executable address ranges of a module from the set of instrumented address ranges using an address belonging to the module.
        
            :param addr: An address contained by module's range.
            
            :returns: True if at least one range was removed from the instrumented ranges.
        """
        pass
    def removeInstrumentedRange(start, end):
        """Remove an address range from the set of instrumented address ranges.
        
            :param start: Start address of the range (included).
            :param end: End address of the range (excluded).
        """
        pass


# PyQBDI class
class pyqbdi():
    def alignedAlloc(size,align):
        """Allocate a block of memory of a specified sized with an aligned base address.
        
            :param size: Allocation size in bytes.
            :param align: Base address alignement in bytes.
            
            :returns: Pointer to the allocated memory or NULL in case an error was encountered.
        """
        pass
    def alignedFree():
        """
        """
        pass
    def allocateVirtualStack(ctx, stackSize):
        """Allocate a new stack and setup the GPRState accordingly.
            The allocated stack needs to be freed with alignedFree().
            
            :param ctx: GPRState which will be setup to use the new stack.
            :param stackSize: Size of the stack to be allocated.
            
            :returns: A tuple (bool, stack) where 'bool' is true if stack allocation was successfull. And 'stack' the newly allocated stack pointer.
        """        
        pass
    def simulateCall(ctx, returnAddress, args):
        """Simulate a call by modifying the stack and registers accordingly.
        
            :param ctx: GPRState where the simulated call will be setup. The state needs to point to a valid stack for example setup with allocateVirtualStack().
            :param returnAddress: Return address of the call to simulate.
            :param args: A list of arguments.
        """
        pass
    def getModuleNames():
        """ Get a list of all the module names loaded in the process memory.
        
            :returns: A list of strings, each one containing the name of a loaded module.
        """
        pass
    def readMemory(address, size):
        """Read a memory content from a base address.
        
            :param address: Base address
            :param size: Read size
            
            :returns: Bytes of content.
        """
        pass
    def writeMemory(address, bytes):
        """Write a memory content to a base address.
        
            :param address: Base address
            :param bytes: Memory content
        """
        pass
    def decodeFloat(ptr):
        """ Decode a float stored as a long.
        
            :param ptr: Long value.
        """
        pass
    def encodeFloat(ptr):
        """Encode a float as a long.
        
            :param ptr: Float value
        """
        pass

# PyQBDI objects

InstAnalysis_Object = None
""" pyInstAnalysis object, a binding to QBDI::InstAnalysis
"""
GPRState_Object = None
""" pyGPRState object, a binding to QBDI::GPRState
"""
FPRState_Object = None
""" pyFPRState object, a binding to QBDI::FPRState
"""
MemoryAccess_Object = None
""" pyMemoryAccess object, a binding to QBDI::MemoryAccess
"""
OperandAnalysis_Object = None
""" pyOperandAnalysis object, a binding to QBDI::OperandAnalysis
"""
VMInstance_Object = None
""" pyVMInstance object, a binding to QBDI::VMInstanceRef
"""
VMState_Object = None
""" pyVMState object, a binding to QBDI::VMState
"""