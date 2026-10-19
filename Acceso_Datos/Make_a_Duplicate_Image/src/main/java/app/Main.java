package app;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {
  public static void main(String[] args) throws IOException {
    Path imagePath = Path.of("src/main/resources/logo.jpg");

    cloneImage(imagePath);
  }

  private static void cloneImage(Path pathOriginal) throws IOException {
    // Get all bites of a image
    byte[] imageBytes = Files.readAllBytes(pathOriginal);

    // Get the file name to make the copy
    String originalName = pathOriginal.getFileName().toString();

    // Convert the file name into a parent File using resolveSibling method
    Path copyPath = pathOriginal.resolveSibling("C_" + originalName); //-> The name of copy will be C_logo.jpg

    Files.write(copyPath, imageBytes);
  }
}
