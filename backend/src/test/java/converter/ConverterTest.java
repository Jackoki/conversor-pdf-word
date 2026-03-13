package converter;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.nio.file.Files;
import java.nio.file.Path;

import org.junit.jupiter.api.Test;

public class ConverterTest {

    @Test
    void shouldConvertPdfToDocx() {

        Converter converter = new Converter();

        Path input = Path.of("src/test/resources/teste.pdf");
        Path outputDir = Path.of("target/test-output");

        converter.convert(input, outputDir);

        Path outputFile = outputDir.resolve("teste.docx");

        assertTrue(Files.exists(outputFile));
    }
}