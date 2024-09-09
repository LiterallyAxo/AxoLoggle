import AxoLoggle
from AxoLoggle import *

# Initialize the logger with default settings
log = AxoLoggle.AxoLoggle()

log.set_level(AxoLoggle.LogLevel.TRACE)

print("\n--- Testing preset logging levels ---")
log.info("This is an INFO message")
log.debug("This is a DEBUG message")
log.warning("This is a WARNING message")
log.error("This is an ERROR message")
log.critical("This is a CRITICAL message")
log.trace("This is a TRACE message")
log.success("This is a SUCCESS message")
log.notice("This is a NOTICE message")
log.alert("This is an ALERT message")

print("\n--- Testing dynamic level enabling/disabling ---")
# Disable DEBUG level, should not print
log.disable_level(LogLevel.DEBUG)
log.debug("This DEBUG message should NOT appear")
# Re-enable DEBUG level, should print
log.enable_level(LogLevel.DEBUG)
log.debug("This DEBUG message should appear after enabling DEBUG again")

print("\n--- Testing custom log levels ---")
# Create a custom log level 'critical_alert' and log with it
log.create_custom_level("critical_alert", 55, color=LogColor.RED)
log.critical_alert("This is a CRITICAL_ALERT log level!")
# Create another custom log level 'minor_warning' and log with it
log.create_custom_level("minor_warning", 29, color=LogColor.YELLOW)
log.minor_warning("This is a MINOR_WARNING log level!")

print("\n--- Testing custom colors for preset levels ---")
# Change the color of the WARNING level
log.set_level_color(LogLevel.WARNING, LogColor.MAGENTA)
log.warning("This is a WARNING message with MAGENTA color")

print("\n--- Testing custom log level removal ---")
# Remove the custom log level 'minor_warning' and try to log with it
log.remove_custom_level("minor_warning")
try:
    log.minor_warning("This should raise an error because the level is removed")
except AttributeError as e:
    print(f"Expected Error: {e}")

print("\n--- Testing global log level setting ---")
# Set global log level to WARNING (INFO and DEBUG should be skipped)
log.set_level(LogLevel.WARNING)
log.info("This INFO message should NOT appear")
log.debug("This DEBUG message should NOT appear")
log.warning("This WARNING message should appear")
log.error("This ERROR message should appear")
log.critical("This CRITICAL message should appear")

print("\n--- Test complete! ---")
