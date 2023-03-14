import os
import sequtils
import strformat
import sugar


proc getThemePaths(): seq[string] =
  let currentDir = getCurrentDir()
  if paramCount() > 0:
    let args = commandLineParams()
    return args.map(arg => joinPath(currentDir, arg))
  else:
    let dirs = joinPath(currentDir, "/*")
    for dir in walkDirs dirs:
      result.add(dir)


func getMasterThemeName(masterThemePath: string): string =
  let themeName = lastPathPart masterThemePath
  fmt"{themeName}-master"


func getMasterThemePath(themeDir: string): string =
  let masterThemeName = getMasterThemeName themeDir
  joinPath(themeDir, masterThemeName)


func hasMasterTheme(themeDir: string): bool =
  let masterThemeDir = getMasterThemePath themeDir
  dirExists masterThemeDir


func getValidThemePaths(themeDirs: seq[string]): seq[string] =
  themeDirs
    .filter(dirExists)
    .filter(hasMasterTheme)


when isMainModule:
  let
    themePaths = getThemePaths()
    validThemePaths = getValidThemePaths themePaths
  
  echo validThemePaths
